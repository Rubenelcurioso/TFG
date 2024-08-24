<template>
  <q-page class="flex flex-center bg-primary text-accent">
    <q-stepper
      v-model="step"
      color="accent"
      animated
      class="bg-purple-2"
    >
      <q-step
        color="primary"
        :name="1"
        title="Business details"
        icon="business"
        :done="step > 1"
      >
        <q-input outlined color="accent" text-color="accent" v-model="businessName" label="Business name" :rules="[
          val => val && val.length > 0 || 'Company name is required',
          val => val.length <= 255 || 'Company name too long'
        ]" />
        <q-input outlined color="accent" text-color="accent" v-model="businessDescription" type="textarea" label="Business description" />
        <q-input outlined color="accent" text-color="accent" v-model="businessEmail" type="email" label="Business email" :rules="[
          val => val && val.length > 0 || 'Email is required',
          val => val.length <= 150 || 'Email too long',
          val => /^\S+@\S+\.\S+$/.test(val) || 'Email is not valid'
        ]" />
        <q-input outlined color="accent" text-color="accent" v-model="businessLocation" label="Business location" />
        <q-input outlined color="accent" text-color="accent" v-model="businessPhone" label="Business phone" :rules="[
          val => !val || val.length <= 20 || 'Phone number too long'
        ]" />
        
        <q-stepper-navigation>
          <q-btn rounded unelevated text-color="accent" @click="step = 2" color="positive" label="Next" />
        </q-stepper-navigation>
      </q-step>

      <q-step
        color="primary"
        :name="2"
        title="Add Employees"
        icon="people"
        :done="step > 2"
      >
        <q-input outlined color="accent" text-color="accent" v-model="searchUser" label="Search User" @update:model-value="onSearchUser">
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>

        <q-list bordered separator class="bg-purple-1">
          <q-item v-for="user in filteredUsers" :key="user.id" clickable v-ripple @click="addUserToEmployees(user)">
            <q-item-section>
              <q-item-label class="text-accent">{{ user }}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>

        <q-list bordered class="q-mt-md" >
          <q-item-label header class="text-accent bg-purple-3">Added Employees</q-item-label>
          <q-item v-for="user in addedEmployees" :key="user.id">
            <q-item-section>
              <q-item-label class="text-accent">{{ user }}</q-item-label>
            </q-item-section>
            <q-item-section side>
              <q-btn flat round color="negative" icon="remove" @click="removeUserFromEmployees(user)" />
            </q-item-section>
          </q-item>
        </q-list>

        <q-stepper-navigation>
          <q-btn  rounded unelevated text-color="accent" flat @click="step = 1" color="warning" label="Back" class="q-mr-sm" />
          <q-btn rounded unelevated text-color="accent" @click="step = 3" color="positive" label="Next" />
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
            <div class="text-h6">Business Details</div>
            <div><strong>Name:</strong> {{ businessName }}</div>
            <div><strong>Description:</strong> {{ businessDescription }}</div>
            <div><strong>Email:</strong> {{ businessEmail }}</div>
            <div><strong>Location:</strong> {{ businessLocation }}</div>
            <div><strong>Phone:</strong> {{ businessPhone }}</div>
          </q-card-section>
        </q-card>

        <q-stepper-navigation>
          <q-btn rounded unelevated text-color="accent" flat @click="step = 1" color="warning" label="Back" class="q-mr-sm" />
          <q-btn rounded unelevated text-color="accent" @click="createBusiness" color="positive" label="Create Business" />
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
  name: 'NewBusiness',
  setup() {
    const step = ref(1)
    const businessName = ref('')
    const businessDescription = ref('')
    const businessEmail = ref('')
    const businessLocation = ref('')
    const businessPhone = ref('')
    const searchUser = ref('')
    const filteredUsers = ref([])
    const addedEmployees = ref([])

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

    const addUserToEmployees = (username) => {
      const currentUser = store.username; // Requester cannot be auto-added
      if (username !== currentUser && !addedEmployees.value.some(u => u === username)) {
        addedEmployees.value.push(username)
      }
    }

    const removeUserFromEmployees = (user) => {
      addedEmployees.value = addedEmployees.value.filter(u => u.id !== user.id)
    }
    const store = useUserStore()
    const router = useRouter()

    const createBusiness = async () => {
      try {
        const businessData = {
          name: businessName.value,
          description: businessDescription.value,
          email: businessEmail.value,
          location: businessLocation.value,
          phone: businessPhone.value,
          owner: store.uid
        };

        const businessResponse = await apiPost('/new/business/', businessData);

        if (businessResponse && businessResponse.id) {
          for (const username of addedEmployees.value) {
            const employeeData = {
              username: username,
              business: businessResponse.id
            };
            await apiPost('/new/employee/', employeeData);
          }
          await router.push(`/home/${store.uid}/business/${businessResponse.id}/`);
        } else {
          throw new Error('Failed to create business');
        }
      } catch (error) {
        console.error('Error creating business:', error);
        // Handle error (e.g., show error message to user)
      }
    }

    return {
      step,
      businessName,
      businessDescription,
      businessEmail,
      businessLocation,
      businessPhone,
      createBusiness,
      onSearchUser,
      addUserToEmployees,
      removeUserFromEmployees,
      searchUser,
      filteredUsers,
      addedEmployees
    }
  }
}
</script>
