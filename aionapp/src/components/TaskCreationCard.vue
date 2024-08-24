<template>
  <q-card class="task-creation-card bg-purple-2">
    <q-toolbar class="bg-purple-3">
      <q-toolbar-title>Add a task</q-toolbar-title>
      <q-btn flat round dense icon="close" @click="closeDialog" color="negative" />
    </q-toolbar>

    <q-form @submit="onSubmit" class="q-gutter-md">
      <q-card-section>
        <q-input outlined color="accent" v-model="taskName" label="Task Name" :rules="taskNameRules" class="text-accent" />
      </q-card-section>

      <q-card-section>
        <div class="row q-col-gutter-md">
          <div class="col-6">
            <q-input outlined color="accent" v-model="startDate" label="Start Date" type="date" :rules="startDateRules" text-color="accent" />
          </div>
          <div class="col-6">
            <q-input outlined color="accent" v-model="endDate" label="End Date" type="date" :rules="endDateRules" text-color="accent" />
          </div>
        </div>
      </q-card-section>

      <q-card-section>
        <div class="text-subtitle2">Priority</div>
        <div class="q-gutter-sm">
          <q-radio keep-color v-model="priority" val="L" label="Low" color="light-blue" class="text-accent" />
          <q-radio keep-color v-model="priority" val="M" label="Medium" color="orange" class="text-accent" />
          <q-radio keep-color v-model="priority" val="H" label="High" color="red" class="text-accent" />  
        </div>
      </q-card-section> 

      <q-card-section>
        <div class="text-subtitle2">Status</div>
        <div class="q-gutter-sm">
          <q-radio keep-color v-model="status" val="TODO" label="To do" color="grey" class="text-accent" />
          <q-radio keep-color v-model="status" val="IN_PROGRESS" label="In progress" color="blue" class="text-accent" />
          <q-radio keep-color v-model="status" val="DONE" label="Done" color="green" class="text-accent" />  
        </div>
      </q-card-section>

      <q-card-section>
        <q-select
          class="text-accent"
          outlined
          color="accent"
          popup-content-class="text-accent bg-purple-1"
          v-model="assignedUser"
          :options="userOptions"
          label="Assign to User"
          :rules="[val => !!val || 'Please assign the task to a user']"
        />
      </q-card-section>

      <q-card-section>
        <q-select
          class="text-accent"
          outlined
          color="accent"
          popup-content-class="text-accent bg-purple-1"
          v-model="assignedTeam"
          :options="teamOptions"
          label="Assign to Team"
        />
      </q-card-section>

      <q-card-actions align="right">
        <q-btn rounded unelevated text-color="accent" type="submit" color="positive" label="Submit" />
      </q-card-actions>
    </q-form>
  </q-card>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { apiGet, apiPost } from '../utils/api-wrapper';
import { useUserStore } from 'stores/user-store';

export default {
  name: 'TaskCreationCard',
  setup(props, { emit }) {
    const taskName = ref('');
    const startDate = ref('');
    const endDate = ref('');
    const priority = ref('L');
    const status = ref('TODO');
    const assignedUser = ref(null);
    const assignedTeam = ref(null);
    const route = useRoute();
    const userOptions = ref([]);
    const teamOptions = ref([]);
    const store = useUserStore();

    const loadUserOptions = async () => {
      const response = await apiGet('/project/'+route.params.pid+'/users/');
      userOptions.value = response.map(user => ({ label: user.username, value: user.id }));
    };

    const loadTeamOptions = async () => {
      const business_id = store.projects.find(project => project.id === parseInt(route.params.pid)).business;
      if(!business_id) return;
      const response = await apiGet(`/business/${business_id}/teams/`);
      teamOptions.value = response.map(team => ({ label: team.name, value: team.id }));
    };

    onMounted(() => {
      loadUserOptions();
      loadTeamOptions();
    });

    const taskNameRules = [
      val => !!val || 'Task name is required'
    ];

    const startDateRules = [
      val => !!val || 'Start date is required',
      val => !endDate.value || val <= endDate.value || 'Start date must be before or equal to end date'
    ];

    const endDateRules = [
      val => !!val || 'End date is required',
      val => !startDate.value || val >= startDate.value || 'End date must be after or equal to start date'
    ];

    const onSubmit = async () => {
      try {
        const taskData = {
          name: taskName.value,
          start_date: startDate.value,
          end_date: endDate.value,
          priority: priority.value,
          project: route.params.pid,
          user_assigned: assignedUser.value.label,
          team_assigned: assignedTeam.value ? assignedTeam.value.value : null,
          status: status.value
        };
        await apiPost('/new/task/', taskData);
        emit('task-created');
      } catch (error) {
        console.error('Error creating task:', error);
      }
    };

    const closeDialog = () => {
      emit('close-d');
    };

    return {
      taskName,
      startDate,
      endDate,
      priority,
      status,
      assignedUser,
      assignedTeam,
      userOptions,
      teamOptions,
      taskNameRules,
      startDateRules,
      endDateRules,
      onSubmit,
      closeDialog
    };
  },
};
</script>

<style scoped lang="scss">
.project-edit-card {
  max-width: 500px;
  margin: 0 auto;
}

::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: $purple-3;
  border-radius: 4px;
}

::-webkit-scrollbar-thumb {
  background: $purple-4;
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>