<template>
  <q-page class="q-pa-md bg-dark text-white">
    <!-- Business Information Section -->
    <q-card dark>
      <q-card-section>
        <div class="text-h6">Business Information</div>
      </q-card-section>

      <q-separator dark />

      <q-card-section>
        <div class="text-h6">{{ business.name }}</div>
        <div class="text-subtitle2">{{ business.location }}</div>
      </q-card-section>

      <q-card-section>
        <q-input v-model="business.description" label="Description" dark />
      </q-card-section>

      <q-card-section>
        <q-input v-model="business.email" label="Email" dark />
      </q-card-section>

      <q-card-section>
        <q-input v-model="business.phone" label="Phone" dark />
      </q-card-section>

      <q-card-actions align="right">
        <q-btn label="Save" color="primary" @click="saveBusiness" />
      </q-card-actions>
    </q-card>

    <!-- Employee Management Section -->
    <q-card class="q-mt-md" dark>
      <q-card-section>
        <div class="text-h6">Employee Management</div>
      </q-card-section>

      <q-separator dark />

      <q-card-section>
        <q-list dark>
          <q-item v-for="employee in employees" :key="employee.id" dark>
            <q-item-section>
              <q-item-label>{{ employee.username }}</q-item-label>
              <q-item-label caption>{{ employee.fullname }}</q-item-label>
              <q-item-label caption>{{ employee.team_name }}</q-item-label>
              <q-separator/>
            </q-item-section>
          </q-item>
        </q-list>
      </q-card-section>

      <q-card-actions align="right">
        <q-btn label="Add Employee" color="primary" @click="addEmployee" />
      </q-card-actions>
    </q-card>

    <!-- Team Management Section -->
    <q-card class="q-mt-md" dark>
      <q-card-section>
        <div class="text-h6">Team Management</div>
      </q-card-section>

      <q-separator dark />

      <q-card-section>
        <!-- Add team management content here -->
        <q-list dark>
          <q-item v-for="team in teams" :key="team.id" clickable v-ripple dark>
            <q-item-section>
              <q-item-label>{{ team.name }}</q-item-label>
              <q-item-label caption>{{ team.members.length }} members</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-card-section>

      <q-card-actions align="right">
        <q-btn label="Create Team" color="primary" @click="createTeam" />
      </q-card-actions>
    </q-card>
  </q-page>
</template>

<script>
import { ref, onMounted } from 'vue'
import { apiGet, apiPut } from '../utils/api-wrapper'
import { useUserStore } from 'stores/user-store'
import { useRoute } from 'vue-router'

export default {
  name: 'BusinessPage',
  setup() {
    const business = ref({})
    const employees = ref([])
    const teams = ref([])
    const store = useUserStore()
    const route = useRoute()

    const fetchBusiness = async () => {
      try {
        const response = await apiGet(`/business/${route.params.bid}/`)
        business.value = response
      } catch (error) {
        console.error('Error fetching business:', error)
      }
    }

    const fetchEmployees = async () => {
      try {
        const response = await apiGet(`/business/${route.params.bid}/employees/`)
        employees.value = response
      } catch (error) {
        console.error('Error fetching employees:', error)
      }
    }

    const fetchTeams = async () => {
      try {
        const response = await apiGet(`/business/${route.params.bid}/teams/`)
        teams.value = response
      } catch (error) {
        console.error('Error fetching teams:', error)
      }
    }

    const saveBusiness = async () => {
      try {
        await apiPut(`/business/${route.params.bid}/`, business.value)
      } catch (error) {
        console.error('Error saving business:', error)
      }
    }

    const addEmployee = () => {
      // Implement add employee functionality
    }

    const createTeam = () => {
      // Implement create team functionality
    }

    onMounted(() => {
      fetchBusiness()
      fetchEmployees()
      fetchTeams()
    })

    return {
      business,
      employees,
      teams,
      store,
      saveBusiness,
      addEmployee,
      createTeam
    }
  }
}
</script>
