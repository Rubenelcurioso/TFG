<template>
  <q-card class="task-edit-card primary">
    <q-toolbar>
      <q-toolbar-title>Edit task</q-toolbar-title>
      <q-btn flat round dense icon="close" @click="closeDialog" />
    </q-toolbar>

    <q-form @submit="onSubmit" class="q-gutter-md">
      <q-card-section>
        <q-input v-model="taskName" label="Task name" :rules="taskNameRules" />
      </q-card-section>

      <q-card-section>
        <div class="row q-col-gutter-md">
          <div class="col-6">
            <q-input v-model="startDate" label="Start date" type="date" :rules="startDateRules" />
          </div>
          <div class="col-6">
            <q-input v-model="endDate" label="End date" type="date" :rules="endDateRules" />
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
        <q-btn type="submit" color="secondary" label="Update" />
      </q-card-actions>
    </q-form>
  </q-card>
</template>

<script>
import { ref, onMounted, inject } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { apiGet, apiPut } from '../utils/api-wrapper';

export default {
  name: 'TaskEditCard',
  props: {
    taskId: {
      type: String,
      required: true
    }
  },
  setup(props, { emit }) {
    const taskName = ref('');
    const startDate = ref('');
    const endDate = ref('');
    const priority = ref('L');
    const status = ref('TODO');
    const assignedUser = ref(null);
    const assignedTeam = ref(null);
    const route = useRoute();
    const router = useRouter();
    const userOptions = ref([]);
    const teamOptions = ref([]);
    const refresh = inject('refresh');

    const loadTaskData = async () => {
      try {
        const response = await apiGet(`/task/${props.taskId}/`);
        taskName.value = response.name;
        startDate.value = response.start_date;
        endDate.value = response.end_date;
        priority.value = response.priority;
        status.value = response.status;
        assignedUser.value = response.user_assigned;
        assignedTeam.value = response.team_assigned;
      } catch (error) {
        console.error('Error loading task data:', error);
      }
    };

    const loadUserOptions = async () => {
      const response = await apiGet('/project/'+route.params.pid+'/users/');
      userOptions.value = response.map(user => ({ label: user.username, value: user.id }));
    };

    const loadTeamOptions = async () => {
      const response = await apiGet('/project/'+route.params.pid+'/teams/');
      teamOptions.value = response.map(team => ({ label: team.name, value: team.id }));
    };

    onMounted(() => {
      loadTaskData();
      loadUserOptions();
      //loadTeamOptions();
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
          user_assigned: assignedUser.value.value,
          team_assigned: assignedTeam.value ? assignedTeam.value.value : null,
          status: status.value
        };
        await apiPut(`/task/${props.taskId}/`, taskData);
        emit('task-updated');
        closeDialog();
      } catch (error) {
        console.error('Error updating task:', error);
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
.task-edit-card {
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
