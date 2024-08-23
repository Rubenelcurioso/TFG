<template>
  <q-page class="q-pa-md">
    <h1>{{ projectName }}</h1>

    <q-tabs
      v-model="tab"
      class="text-teal"
      align="left"
    >
      <q-tab name="properties" label="Properties" />
      <q-tab name="tasks" label="Tasks" />
    </q-tabs>

    <q-tab-panels v-model="tab" animated>
      <q-tab-panel name="properties">
        <ProjectInfo
          :pid=Number(route.params.pid)
          :description="description"
          :createdAt=createdAt
          :endDate=endDate
          :progress="progress"
          :linkedBusiness="linkedBusiness"
          :editProjectDialog="editProjectDialog"
        />
      </q-tab-panel>

      <q-tab-panel name="tasks">
        <TaskTable />      
      </q-tab-panel>
    </q-tab-panels>

  </q-page>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import TaskTable from 'components/TaskTable.vue';
import ProjectInfo from 'components/ProjectInfo.vue';
import { apiGet } from '../utils/api-wrapper';
import { useUserStore } from 'stores/user-store';

export default defineComponent({
  name: 'ProjectPage',
  components: {
    TaskTable,
    ProjectInfo
  },
  setup() {
    const route = useRoute();
    const tab = ref('properties')
    const projectName = ref('')
    const projectId = ref(route.params.pid)    
    const createdAt = ref('')
    const endDate = ref('')
    const description = ref('')
    const progress = ref(0.00)
    const linkedBusiness = ref('')
    const store = useUserStore();

    const fetchProjectData = async () => {
      const response = await apiGet('/project/'+projectId.value+'/');
      projectName.value = response.name;
      createdAt.value = response.start_date;
      endDate.value = response.end_date;
      description.value = response.description;
      progress.value = response.progress;
      linkedBusiness.value = response.business_name;
    }

    onMounted(fetchProjectData);

    return {
      tab,
      projectName,
      createdAt,
      endDate,
      progress,
      description,
      route,
      linkedBusiness
    }
  }
});
</script>
