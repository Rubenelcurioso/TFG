<template>
  <q-dialog v-model="dialogOpen" persistent>
    <q-card class="bg-dark text-white">
      <q-card-section>
        <q-input dark v-model="searchUser" label="Search User" @update:model-value="onSearchUser">
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>

        <q-list bordered separator dark>
          <q-item v-for="user in filteredUsers" :key="user.id" clickable v-ripple @click="addUserToProject(user)">
            <q-item-section>
              <q-item-label>{{ user }}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>

        <q-list bordered class="q-mt-md" dark>
          <q-item-label header>Added members</q-item-label>
          <q-item v-for="user in addedMembers" :key="user.id">
            <q-item-section>
              <q-item-label>{{ user.username }}</q-item-label>
              <q-select
                v-model="user.role"
                :options="roleOptions"
                option-value="value"
                option-label="label"
                label="Role"
                dense
                options-dense
                dark
                style="min-width: 100px;"
                @update:model-value="updateUserRole(user)"
              />
            </q-item-section>
            <q-item-section side>
              <q-btn flat round color="negative" icon="remove" @click="removeUserFromProject(user)" />
            </q-item-section>
          </q-item>
        </q-list>
      </q-card-section>

      <q-card-actions align="right">
        <q-btn label="Add" color="primary" @click="onSubmit" />
        <q-btn flat label="Close" color="primary" v-close-popup @click="closeDialog" />
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script>
import { ref, onMounted } from 'vue'
import { apiGet, apiPut, apiDelete } from '../utils/api-wrapper'
import { useUserStore } from 'stores/user-store';

export default {
  name: 'NewUserProject',
  props: {
    pid: {
      type: Number,
      required: true
    },
    users: {
      type: Array,
      required: true
    }
  },
  setup(props, { emit }) {
    const dialogOpen = ref(true)
    const searchUser = ref('')
    const filteredUsers = ref([])
    const addedMembers = ref([])
    const userStore = useUserStore();
    const roleOptions = ref([])
    const model = ref(null)

    const fetchRoles = async () => {
      try {
        const response = await apiGet('/roles/');
        roleOptions.value = response
          .filter(role => role.name.toLowerCase() !== 'owner')
          .map(role => ({ value: role.id, label: role.name }));   
      } catch (error) {
        console.error('Error fetching roles:', error);
      }
    }

    fetchRoles();

    const onSearchUser = async (val) => {
      if (val.length >= 3) {
        try {
          const response = await apiGet('/username/' + encodeURIComponent(val) + '/');
          filteredUsers.value = response;
        } catch (error) {
          console.error('Error searching for users:', error);
        }
      } else {
        filteredUsers.value = [];
      }
    }

    const addUserToProject = (user) => {
      const currentUser = userStore.username;
      if (currentUser !== user && !addedMembers.value.some(u => u.username === user)) {
        const defaultRole = roleOptions.value[2];
        addedMembers.value.push({username: user, role: defaultRole});
      }
    }

    const removeUserFromProject = async (user) => {
      const userStore = useUserStore();
      const projectRolePerm = userStore.projects.find(project => project.id === props.pid)?.role_perm;

      if (projectRolePerm >= 31) {
        const userToRemove = addedMembers.value.find(u => u.username === user.username);
        if (userToRemove && projectRolePerm > userToRemove.role_perm) {
          const response = await apiDelete(`/remove/user/${user.username}/${props.pid}/`);
          addedMembers.value = addedMembers.value.filter(u => u.username !== user.username);
          emit('user-mod');
        } else {
          console.warn('Cannot remove user with equal or higher role permission');
        }
      } else {
        console.warn('Insufficient permissions to remove user from project');
      }
    }

    const updateUserRole = (user) => {
      const updatedUser = addedMembers.value.find(u => u.username === user.username);
      if (updatedUser) {
        updatedUser.role = user.role.label;
      }
    }

    const onSubmit = async () => {
      for (const user of addedMembers.value) {
        if(user.role !== undefined){
          const role_id = roleOptions.value.find(option => option.label === user.role);
          if(role_id !== undefined){
            try {
              const userData = {
              user: user.username,
              project: props.pid,
              role: role_id.value
              };
              const response = await apiPut('/userprojectrole/update/', userData);
            } catch (error) {
              console.error(`Error adding user ${user.username} to project:`, error);
            }
          }
        }
      }
      dialogOpen.value = false;
      emit('user-mod');
    }

    const closeDialog = () => {
      dialogOpen.value = false;
      emit('close-dialog');
    }

    const updateAddedMembers = () => {
      addedMembers.value = props.users.map(user => ({
        ...user,
        role: roleOptions.value.find(role => role.value === user.role) || roleOptions.value[2]
      }));
    }

    onMounted(() => {
      updateAddedMembers();
    });

    return {
      dialogOpen,
      searchUser,
      filteredUsers,
      addedMembers,
      onSearchUser,
      addUserToProject,
      removeUserFromProject,
      updateUserRole,
      onSubmit,
      closeDialog,
      model,
      roleOptions
    }
  }
}
</script>
