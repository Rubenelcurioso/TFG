<template>
  <div>
    <div class="text-h6">Project Properties</div>
    <q-btn label="Edit Project" color="primary" @click="editProjectDialog" />
    <p>Project description: {{ description }}</p>
    <p>Created at: {{ createdAt }}</p>
    <p>End date: {{ endDate }}</p>
    <p>Progress: {{ progress }}</p>
    <p>Linked business: {{ linkedBusiness }}</p>
  </div>

  <q-dialog v-model="editDialogVisible">
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
