<template>
  <div class="bg-purple-1">
    <div class="text-h6 text-accent">Project properties</div>
    <p class="text-accent">Created at: {{ createdAt }}</p>
    <p class="text-accent">End date: {{ endDate }}</p>
    <p class="text-accent">Progress: {{ progress }} %</p>
    <p class="text-accent">Linked business: {{ linkedBusiness }}</p>
    <q-btn rounded outline label="Edit Project" color="info" @click="editProjectDialog" class="text-accent" style="position: absolute; bottom: 10px; right: 10px; padding: 10px; margin: 10px; color: black;" />
  </div>

  <q-dialog v-model="editDialogVisible" backdrop-filter="blur(10px)">
      <ProjectEditCard
        :projectId=project_id
        @project-updated="onProjectUpdated"
        @close-dialog="editDialogVisible = false"
      />
    </q-dialog>
</template>

<script>
import { defineComponent, ref } from 'vue';
import { useUserStore } from 'stores/user-store';
import ProjectEditCard from 'components/ProjectEditCard.vue';

export default defineComponent({
  name: 'ProjectInfo',
  props: {
    pid: Number,
    description: String,
    createdAt: Date,
    endDate: Date,
    progress: Number,
    linkedBusiness: String
  },
  components:{
    ProjectEditCard
  },
  setup(props){
    const project_id = props.pid;
    const description = props.description;
    const createdAt = props.createdAt;
    const endDate = props.endDate;
    const progress = props.progress;
    const linkedBusiness = props.business;
    const editDialogVisible = ref(false);
    const store = useUserStore();

    const editProjectDialog = () => {
      if(store.projects.find(project => project.id === project_id).role_perm >= 63){
        editDialogVisible.value = true;
      }
    };

    const onProjectUpdated = () => {
      editDialogVisible.value = false;
    }


    return{
      editDialogVisible,
      editProjectDialog,
      onProjectUpdated,
      project_id
    }
  }
});
</script>
