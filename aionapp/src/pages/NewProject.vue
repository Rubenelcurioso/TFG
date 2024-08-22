<template>
  <q-page class="flex flex-center bg-dark text-white">
    <q-stepper
      v-model="step"
      color="primary"
      animated
      dark
    >
      <q-step
        :name="1"
        title="Project Details"
        icon="assignment"
        :done="step > 1"
      >
        <q-input v-model="projectName" label="Project Name" dark />
        <q-input v-model="projectDescription" type="textarea" label="Project Description" dark />
        <q-input v-model="startDate" type="date" label="Start Date" dark />
        <q-input v-model="endDate" type="date" label="End Date" dark />
        
        <q-stepper-navigation>
          <q-btn @click="step = 2" color="primary" label="Next" />
        </q-stepper-navigation>
      </q-step>

      <q-step
        :name="2"
        title="Add Users"
        icon="people"
        :done="step > 2"
      >
        <q-input v-model="searchUser" label="Search User" @update:model-value="onSearchUser" dark>
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
          <q-item-label header>Added Users</q-item-label>
          <q-item v-for="user in addedUsers" :key="user.id">
            <q-item-section>
              <q-item-label>{{ user.username }}</q-item-label>
              <q-select
                v-model="model"
                :options="roleOptions"
                label="Role"
                dense
                options-dense
                dark
                style="min-width: 50px;"
              />
            </q-item-section>
            <q-item-section side>
              <q-btn flat round color="negative" icon="remove" @click="removeUserFromProject(user)" />
            </q-item-section>
          </q-item>
        </q-list>

        <q-stepper-navigation>
          <q-btn flat @click="step = 1" color="primary" label="Back" class="q-mr-sm" />
          <q-btn @click="createProject" color="primary" label="Create Project" />
        </q-stepper-navigation>
      </q-step>
    </q-stepper>
  </q-page>
</template>

<script>
import { ref } from 'vue'
import { apiPost, apiGet } from '../utils/api-wrapper'
import { useUserStore } from 'stores/user-store';
import { useRouter } from 'vue-router'

export default {
  name: 'NewProject',
  setup() {
    const step = ref(1)
    const projectName = ref('')
    const projectDescription = ref('')
    const startDate = ref('')
    const endDate = ref('')
    const searchUser = ref('')
    const filteredUsers = ref([])
    const addedUsers = ref([])
    const roleOptions = ref([])
    const model = ref(null)

    const fetchRoles = async () => {
      try {
        const response = await apiGet('/roles/');
        roleOptions.value = response
          .filter(role => role.name.toLowerCase() !== 'owner')
          .map(role => ({ value: role.id, label: role.name }));      
      } 
        catch (error) {
        console.error('Error fetching roles:', error);
      }
    }

    fetchRoles();
    const store = useUserStore()
    const router = useRouter()

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

    const addUserToProject = (username) => {
      const currentUser = store.username; // Requester cannot be auto-added
      if (username !== currentUser && !addedUsers.value.some(u => u === username)) {
        addedUsers.value.push({ username, role: roleOptions.value[0].value })
      }
    }

    const removeUserFromProject = (user) => {
      addedUsers.value = addedUsers.value.filter(u => u.id !== user.id)
    }

    const createProject = async () => {
      try {
        const projectData = {
          name: projectName.value,
          description: projectDescription.value,
          start_date: startDate.value,
          end_date: endDate.value,
          owner_id: store.uid,
        };

        const projectResponse = await apiPost('/new/project/', projectData);

        if (projectResponse && projectResponse.id) {
          for (const user of addedUsers.value) {
            const userProjectRoleData = {
              user: user.username,
              project: projectResponse.id,
              role: user.role
            };
            await apiPost('/userprojectrole/', userProjectRoleData);
          }
          await router.push(`/home/${store.uid}/project/${projectResponse.id}/`);
        } else {
          throw new Error('Failed to create project');
        }
      } catch (error) {
        console.error('Error creating project:', error);
        // Handle error (e.g., show error message to user)
      }
    }

    return {
      step,
      projectName,
      projectDescription,
      startDate,
      endDate,
      searchUser,
      filteredUsers,
      addedUsers,
      onSearchUser,
      addUserToProject,
      removeUserFromProject,
      createProject,
      model,
      roleOptions
    }
  }
}
</script>
