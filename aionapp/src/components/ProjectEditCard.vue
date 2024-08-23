<template>
  <q-card class="project-edit-card bg-dark text-white">
    <q-toolbar class="bg-secondary">
      <q-toolbar-title>Edit project</q-toolbar-title>
      <q-btn flat round dense icon="close" @click="closeDialog" color="white" />
    </q-toolbar>

    <q-form @submit="onSubmit" class="q-gutter-md">
      <q-card-section>
        <q-input v-model="projectName" label="Project name" :rules="projectNameRules" dark />
      </q-card-section>

      <q-card-section>
        <div class="row q-col-gutter-md">
          <div class="col-6">
            <q-input v-model="startDate" label="Start date" type="date" :rules="startDateRules" dark />
          </div>
          <div class="col-6">
            <q-input v-model="endDate" label="End date" type="date" :rules="endDateRules" dark />
          </div>
        </div>
      </q-card-section>

      <q-card-section>
        <q-select
          v-model="selectedBusiness"
          :options="businesses"
          label="Select business"
          option-value="value"
          option-label="label"
          emit-value
          map-options
          dark
        />
      </q-card-section>

      <q-card-section>
        <q-input v-model="description" label="Description" type="textarea" dark />
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
import { useUserStore } from 'stores/user-store';
import { apiGet, apiPut } from '../utils/api-wrapper';

export default {
  name: 'ProjectEditCard',
  props: {
    projectId: {
      type: String,
      required: true
    }
  },
  setup(props, { emit }) {
    const projectName = ref('');
    const startDate = ref('');
    const endDate = ref('');
    const description = ref('');
    const projectManager = ref(null);
    const route = useRoute();
    const store = useUserStore();
    const userOptions = ref([]);
    const refresh = inject('refresh');

    const userStore = useUserStore();
    const businesses = ref([]);
    const selectedBusiness = ref(null);

    const loadProjectData = async () => {
      try {
        const response = await apiGet(`/project/${props.projectId}/`);
        projectName.value = response.name;
        startDate.value = response.start_date;
        endDate.value = response.end_date;
        description.value = response.description;
        selectedBusiness.value = response.business.id;
      } catch (error) {
        console.error('Error loading project data:', error);
      }
    };

    onMounted(() => {
      loadProjectData();
      businesses.value = userStore.businesses.map(business => ({
        value: business.id,
        label: business.name
      }));
    });

    const projectNameRules = [
      val => !!val || 'Project name is required'
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
      if(store.projects.find(project => project.id === props.projectId).role_perm < 63){
        emit('project-updated');
        closeDialog();
      }else{
          try {
          const projectData = {
            project_id: props.projectId,
            name: projectName.value,
            start_date: startDate.value,
            end_date: endDate.value,
            description: description.value,
            project_manager: projectManager.value,
            business: selectedBusiness.value
          };
          await apiPut(`/project/update/`, projectData);
          emit('project-updated');
          closeDialog();
        } catch (error) {
          console.error('Error updating project:', error);
        }
      }
      
    };

    const closeDialog = () => {
      emit('close-dialog');
    };

    return {
      projectName,
      startDate,
      endDate,
      description,
      projectManager,
      userOptions,
      businesses,
      selectedBusiness,
      projectNameRules,
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
