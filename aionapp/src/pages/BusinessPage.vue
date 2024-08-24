<template>
  <q-page class="q-pa-md bg-dark text-white">
    <q-card dark>
      <q-card-section>
        <div class="text-h6">Business information</div>
      </q-card-section>

      <q-separator dark />

      <q-card-section>
        <div class="text-h6">{{ business.name }}</div>
        <div class="text-subtitle2">{{ business.location }}</div>
      </q-card-section>

      <q-card-section>
        <q-input v-model="business.description" label="Description" dark :readonly="!isOwner" />
      </q-card-section>

      <q-card-section>
        <q-input v-model="business.email" label="Email" dark :readonly="!isOwner" />
      </q-card-section>

      <q-card-section>
        <q-input v-model="business.phone" label="Phone" dark :readonly="!isOwner" />
      </q-card-section>

      <q-card-actions align="right" v-if="isOwner">
        <q-btn label="Save" color="primary" @click="saveBusiness" />
      </q-card-actions>
    </q-card>

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
            </q-item-section>
            <q-item-section side v-if="isOwner">
              <q-btn flat round color="negative" icon="delete" @click="deleteEmployee(employee.username)" />
            </q-item-section>
          </q-item>
        </q-list>
      </q-card-section>

      <q-card-actions align="right" v-if="isOwner">
        <q-btn label="Add Employee" color="primary" @click="showNewEmployeeDialog = true" />
        <NewEmployee v-model="showNewEmployeeDialog" :bid="route.params.bid" @employee-added="showNewEmployeeDialog = false" />
      </q-card-actions>
    </q-card>

    <q-card class="q-mt-md" dark>
      <q-card-section>
        <div class="text-h6">Team Management</div>
      </q-card-section>

      <q-separator dark />

      <q-card-section>
        <q-list dark>
          <q-item v-for="team in teams" :key="team.id" clickable v-ripple dark @click="openTeamEditDialog(team)">
            <q-item-section>
              <q-item-label>{{ team.name }}</q-item-label>
            </q-item-section>
            <q-item-section side v-if="isOwner">
              <q-btn flat round color="negative" icon="delete" @click.stop="deleteTeam(team.id)" />
            </q-item-section>
          </q-item>
        </q-list>
      </q-card-section>

      <q-card-actions align="right" v-if="isOwner">
        <q-btn label="Add Team" color="primary" @click="showNewTeamDialog = true" />
        <NewTeam v-model="showNewTeamDialog" :bid="route.params.bid" @team-created="showNewTeamDialog = false" />
      </q-card-actions>
    </q-card>

    <q-dialog v-model="editDialogVisible">
      <TeamEditCard :team="selectedTeam" :bid="route.params.bid" @team-updated="editDialogVisible = false" @close-dialog="editDialogVisible = false" />
    </q-dialog>
    
  </q-page>
</template>

<script>
import { ref, onMounted, computed } from 'vue'
import { apiGet, apiPut, apiDelete } from '../utils/api-wrapper'
import { useUserStore } from 'stores/user-store'
import { useRoute } from 'vue-router'
import NewTeam from 'components/NewTeam.vue'
import NewEmployee from 'components/NewEmployee.vue'
import TeamEditCard from 'components/TeamEditCard.vue'

export default {
  name: 'BusinessPage',
  components:{
    NewTeam,
    NewEmployee,
    TeamEditCard
  },
  setup() {
    const business = ref({})
    const employees = ref([])
    const teams = ref([])
    const store = useUserStore()
    const route = useRoute()
    const editDialogVisible = ref(false)
    const showNewTeamDialog = ref(false)
    const showNewEmployeeDialog = ref(false)
    const selectedTeam = ref(null)

    const isOwner = computed(() => {
      return store.businesses.some(business => business.id == route.params.bid && business.owner === store.uid)
    })

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

    const deleteEmployee = async (employee) => {
      if (!isOwner.value) return
      try {
        await apiDelete(`/remove/employee/${route.params.bid}/${employee}/`)
        fetchEmployees()
      } catch (error) {
        console.error('Error deleting employee:', error)
      }
    }

    const deleteTeam = async (teamId) => {
      if (!isOwner.value) return
      try {
        await apiDelete(`/remove/team/${route.params.bid}/${teamId}/`)
        fetchTeams()
      } catch (error) {
        console.error('Error deleting team:', error)
      }
    }

    const saveBusiness = async () => {
      if (!isOwner.value) return
      try {
        const businessData = {
          business: route.params.bid,
          name: business.value.name,
          description: business.value.description,
          phone: business.value.phone,
          email: business.value.email,
        }
        await apiPut(`/business/update/`, businessData)
      } catch (error) {
        console.error('Error saving business:', error)
      }
    }

    const openTeamEditDialog = (team) => {
      if (!isOwner.value) return
      selectedTeam.value = team.id
      editDialogVisible.value = true
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
      NewTeam,
      NewEmployee,
      TeamEditCard,
      showNewTeamDialog,
      showNewEmployeeDialog,
      route,
      deleteEmployee,
      deleteTeam,
      editDialogVisible,
      selectedTeam,
      openTeamEditDialog,
      isOwner
    }
  }
}
</script>
