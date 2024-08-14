<template>
  <q-page class="flex flex-center">
    <q-stepper
      v-model="step"
      color="primary"
      animated
    >
      <q-step
        :name="1"
        title="Project Details"
        icon="assignment"
        :done="step > 1"
      >
        <q-input v-model="projectName" label="Project Name" />
        <q-input v-model="projectDescription" type="textarea" label="Project Description" />
        <q-input v-model="startDate" type="date" label="Start Date" />
        <q-input v-model="endDate" type="date" label="End Date" />
        
        <q-stepper-navigation>
          <q-btn @click="step = 2" color="dark" label="Next" />
        </q-stepper-navigation>
      </q-step>

      <q-step
        :name="2"
        title="Add Users"
        icon="people"
        :done="step > 2"
      >
        <q-input v-model="searchUser" label="Search User" @input="onSearchUser">
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>

        <q-list bordered separator>
          <q-item v-for="user in filteredUsers" :key="user.id" clickable v-ripple @click="addUserToProject(user)">
            <q-item-section>
              <q-item-label>{{ user.name }}</q-item-label>
              <q-item-label caption>{{ user.email }}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>

        <q-list bordered class="q-mt-md">
          <q-item-label header>Added Users</q-item-label>
          <q-item v-for="user in addedUsers" :key="user.id">
            <q-item-section>
              <q-item-label>{{ user.name }}</q-item-label>
              <q-item-label caption>{{ user.email }}</q-item-label>
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
import { apiPost } from '../utils/api-wrapper'

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

    const onSearchUser = (val) => {
      // Implement user search logic here
      // This is a placeholder, replace with actual API call
      filteredUsers.value = [
        { id: 1, name: 'John Doe', email: 'john@example.com' },
        { id: 2, name: 'Jane Smith', email: 'jane@example.com' },
      ].filter(user => user.name.toLowerCase().includes(val.toLowerCase()))
    }

    const addUserToProject = (user) => {
      if (!addedUsers.value.some(u => u.id === user.id)) {
        addedUsers.value.push(user)
      }
    }

    const removeUserFromProject = (user) => {
      addedUsers.value = addedUsers.value.filter(u => u.id !== user.id)
    }

    const createProject = () => {
      // Implement project creation logic here
      apiPost('/new/project/', {
        name: projectName.value,
        description: projectDescription.value,
        start_date: startDate.value,
        end_date: endDate.value,
      });
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
      createProject
    }
  }
}
</script>
