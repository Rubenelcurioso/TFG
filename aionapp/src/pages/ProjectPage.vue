<template>
  <q-page class="q-pa-md bg-primary">
    <h3 class="text-accent q-mb-sm">{{ projectName }}</h3>
    <h5 class="courier-font q-mb-sm">{{ description }}</h5>

    <q-tabs
      v-model="tab"
      class="text-accent bg-purple-3 justify-center q-mb"
      align="center"
      indicator-color="info"
      active-color="info"
      active-bg-color="purple-2"
      dense
    >
      <q-tab name="properties" label="Properties" />
      <q-tab name="tasks" label="Tasks" />
      <q-tab name="userManagement" label="User Management" />
      <q-tab name="charts" label="Charts" />
    </q-tabs>

    <q-tab-panels v-model="tab" animated>
      <q-tab-panel name="properties" class="bg-purple-1">
        <ProjectInfo
          :pid=Number(route.params.pid)
          :description="description"
          :createdAt=createdAt
          :endDate=endDate
          :progress="progress"
          :linkedBusiness="linkedBusiness"
        />
      </q-tab-panel>

      <q-tab-panel name="tasks" class="bg-purple-1">
        <TaskTable />      
      </q-tab-panel>
      <q-tab-panel name="userManagement" class="bg-purple-1">
        <UserProjectManagement
          :pid=Number(route.params.pid)
        />
      </q-tab-panel>


      <q-tab-panel name="charts" class="bg-purple-1">
        <ApexCharts
          :pid=Number(route.params.pid)
        />
      </q-tab-panel>
    </q-tab-panels>

  </q-page>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import TaskTable from 'components/TaskTable.vue';
import ProjectInfo from 'components/ProjectInfo.vue';
import UserProjectManagement from 'components/UserProjectManagement.vue';
import ApexCharts from 'components/ApexCharts.vue';
import { apiGet } from '../utils/api-wrapper';
import { useUserStore } from 'stores/user-store';

export default defineComponent({
  name: 'ProjectPage',
  components: {
    TaskTable,
    ProjectInfo,
    UserProjectManagement,
    ApexCharts
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
