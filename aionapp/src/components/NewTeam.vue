<template>
  <q-dialog v-model="dialogOpen" persistent backdrop-filter="blur(10px)">
    <q-card class="bg-dark text-white">
      <q-stepper
        v-model="step"
        color="accent"
        animated
        dark
        class="bg-purple-2"
      >
      <q-step
        color="primary"
        :name="1"
        title="Team Details"
        icon="people"
        :done="step > 1"
      >
        <q-input outlined color="accent" text-color="accent" v-model="teamName" label="Team Name" :rules="[
          val => val && val.length > 0 || 'Team name is required',
          val => val.length <= 255 || 'Team name too long'
        ]" />
        <q-input outlined color="accent" text-color="accent" v-model="teamDescription" type="textarea" label="Team Description" />
        
        <q-stepper-navigation>
          <q-btn rounded unelevated @click="step = 2" color="positive" text-color="accent" label="Next" />
        </q-stepper-navigation>
      </q-step>

      <q-step
        color="primary"
        :name="2"
        title="Add Members"
        icon="person_add"
        :done="step > 2"
      >
        <q-input outlined color="accent" text-color="accent" v-model="searchUser" label="Search User" @update:model-value="onSearchUser">
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>

        <q-list bordered separator class="bg-purple-2">
          <q-item v-for="user in filteredUsers" :key="user.id" clickable v-ripple @click="addUserToTeam(user)">
            <q-item-section>
              <q-item-label class="text-accent">{{ user }}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>

        <q-list bordered class="q-mt-md bg-purple-2">
          <q-item-label header class="text-accent bg-purple-3">Added Members</q-item-label>
          <q-item v-for="user in addedMembers" :key="user.id">
            <q-item-section>
              <q-item-label class="text-accent">{{ user }}</q-item-label>
            </q-item-section>
            <q-item-section side>
              <q-btn  flat round color="negative" icon="remove" @click="removeUserFromTeam(user)" />
            </q-item-section>
          </q-item>
        </q-list>

        <q-stepper-navigation>
          <q-btn rounded unelevated @click="step = 1" color="warning" text-color="accent" label="Back" class="q-mr-sm" />
          <q-btn rounded unelevated @click="step = 3" color="positive" text-color="accent" label="Next" />
        </q-stepper-navigation>
      </q-step>

      <q-step
        color="primary"
        :name="3"
        title="Confirmation"
        icon="check"
        :done="step > 3"
      >
        <q-card class="bg-purple-1">
          <q-card-section class="text-accent">
            <div class="text-h6">Team Details</div>
            <div><strong>Name:</strong> {{ teamName }}</div>
            <div><strong>Description:</strong> {{ teamDescription }}</div>
          </q-card-section>
        </q-card>

        <q-stepper-navigation>
          <q-btn rounded unelevated @click="step = 1" color="warning" text-color="accent" label="Back" class="q-mr-sm" />
          <q-btn rounded unelevated @click="createTeam" color="positive" text-color="accent" label="Create Team" />
        </q-stepper-navigation>
      </q-step>
    </q-stepper>
    <q-card-actions align="right" class="bg-purple-3">
      <q-btn  rounded flat label="Close" color="negative" v-close-popup />
    </q-card-actions>
  </q-card>
  </q-dialog>
</template>

<script>
import { ref } from 'vue'
import { apiPost, apiGet, apiPut } from '../utils/api-wrapper'
import { useUserStore } from 'stores/user-store';

export default {
  name: 'NewTeam',
  props: {
    bid: {
      type: String,
      required: true
    }
  },
  setup(props) {
    const dialogOpen = ref(true)
    const step = ref(1)
    const teamName = ref('')
    const teamDescription = ref('')
    const searchUser = ref('')
    const filteredUsers = ref([])
    const addedMembers = ref([])


    const onSearchUser = async (val) => {
      if (val.length >= 3) {
        try {
          const response = await apiGet('/employees/username/'+ props.bid + '/' + encodeURIComponent(val) + '/');
          filteredUsers.value = response;
        } catch (error) {
          console.error('Error searching for users:', error);
        }
      } else {
        filteredUsers.value = [];
      }
    }

    const addUserToTeam = (username) => {
      if (!addedMembers.value.some(u => u === username)) {
        addedMembers.value.push(username);
      }
    }

    const removeUserFromTeam = (user) => {
      addedMembers.value = addedMembers.value.filter(u => u.id !== user.id)
    }

    const store = useUserStore()

    const createTeam = async () => {
      try {
        const teamData = {
          name: teamName.value,
          description: teamDescription.value,
          business: props.bid
        };

        const teamResponse = await apiPost('/new/team/', teamData);

        if (teamResponse && teamResponse.id) {
          for (const username of addedMembers.value) {
            const memberData = {
              business: props.bid,
              username: username,
              team: teamResponse.id
            };
            await apiPut('/new/member/', memberData);
          }
          dialogOpen.value = false;
          $emit('team-created');
        } else {
          throw new Error('Failed to create team');
        }
      } catch (error) {
        console.error('Error creating team:', error);
        // Handle error (e.g., show error message to user)
      }
    }

    return {
      dialogOpen,
      step,
      teamName,
      teamDescription,
      searchUser,
      filteredUsers,
      addedMembers,
      onSearchUser,
      addUserToTeam,
      removeUserFromTeam,
      createTeam
    }
  }
}
</script>
