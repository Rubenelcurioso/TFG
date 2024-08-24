<template>
  <q-card class="task-creation-card primary">
    <q-toolbar>
      <q-toolbar-title>Add a task</q-toolbar-title>
      <q-btn flat round dense icon="close" @click="closeDialog" />
    </q-toolbar>

    <q-form @submit="onSubmit" class="q-gutter-md">
      <q-card-section>
        <q-input v-model="taskName" label="Task Name" :rules="taskNameRules" />
      </q-card-section>

      <q-card-section>
        <div class="row q-col-gutter-md">
          <div class="col-6">
            <q-input v-model="startDate" label="Start Date" type="date" :rules="startDateRules" />
          </div>
          <div class="col-6">
            <q-input v-model="endDate" label="End Date" type="date" :rules="endDateRules" />
          </div>
        </div>
      </q-card-section>

      <q-card-section>
        <div class="text-subtitle2">Priority</div>
        <div class="q-gutter-sm">
          <q-radio keep-color v-model="priority" val="L" label="Low" color="light-blue" />
          <q-radio keep-color v-model="priority" val="M" label="Medium" color="orange" />
          <q-radio keep-color v-model="priority" val="H" label="High" color="red" />  
        </div>
      </q-card-section> 

      <q-card-section>
        <div class="text-subtitle2">Status</div>
        <div class="q-gutter-sm">
          <q-radio keep-color v-model="status" val="TODO" label="To do" color="grey" />
          <q-radio keep-color v-model="status" val="IN_PROGRESS" label="In progress" color="blue" />
          <q-radio keep-color v-model="status" val="DONE" label="Done" color="green" />  
        </div>
      </q-card-section>

      <q-card-section>
        <q-select
          v-model="assignedUser"
          :options="userOptions"
          label="Assign to User"
          :rules="[val => !!val || 'Please assign the task to a user']"
        />
      </q-card-section>

      <q-card-section>
        <q-select
          v-model="assignedTeam"
          :options="teamOptions"
          label="Assign to Team"
        />
      </q-card-section>

      <q-card-actions align="right">
        <q-btn type="submit" color="secondary" label="Submit" />
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
  emits: ['task-created', 'close-dialog'],
  setup({ emit }) {
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
        closeDialog();
      } catch (error) {
        console.error('Error creating task:', error);
      }
    };

    const closeDialog = () => {
      emit('close-dialog');
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
.task-creation-card {
  max-width: 500px;
  margin: 0 auto;
}

::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 4px;
}

::-webkit-scrollbar-thumb {
  background: $dark;
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>
