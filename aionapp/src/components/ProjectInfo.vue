<template>
  <div class="bg-white">
    <div class="text-h6 text-accent">Project properties</div>
    <q-separator color="#FF0000" inset size="2px"/>
    <p class="text-accent q-mt-md q-mb-none sans-serif">Created at</p>
    <q-input standout v-model="creationDate" label="" class="text-accent bg-primary" readonly/>
    <p class="text-accent q-mt-sm q-mb-none sans-serif">End date</p>
    <q-input standout v-model="endingDate" label=" " class="text-accent bg-primary" readonly/>
    <p class="text-accent q-mt-sm q-mb-none sans-serif">Progress: {{ progression }}%</p>
    <q-linear-progress :value="progression/100" size="20px" rounded color="info" class="q-mt-sm q-mb-sm" />
    <p class="text-accent q-mt-sm q-mb-none sans-serif">Business</p>
    <q-input standout v-model="businessName" label=" " class="text-accent bg-primary generic-border-radius" readonly/>
    <q-btn push label="Edit Project" color="dark" @click="editProjectDialog" class="text-accent q-mt-md" />
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
import { defineComponent, ref, watch } from 'vue';
import { useUserStore } from 'stores/user-store';
import ProjectEditCard from 'components/ProjectEditCard.vue';

export default defineComponent({
  name: 'ProjectInfo',
  props: {
    pid: Number,
    description: String,
    createdAt: String,
    endDate: String,
    progress: Number,
    linkedBusiness: String
  },
  components:{
    ProjectEditCard
  },
  setup(props){
    const project_id = props.pid;
    const description = ref(props.description);
    const creationDate = ref(props.createdAt);
    const endingDate = ref(props.endDate);
    const progression = ref(props.progress);
    const businessName = ref(props.business);
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

    watch(() => props.description, (newVal) => {
      description.value = newVal;
    });

    watch(() => props.createdAt, (newVal) => {
      creationDate.value = newVal;
    });

    watch(() => props.endDate, (newVal) => {
      endingDate.value = newVal;
    });

    watch(() => props.progress, (newVal) => {
      progression.value = newVal;
    });

    watch(() => props.linkedBusiness, (newVal) => {
      businessName.value = newVal;
    });

    return{
      creationDate,
      endingDate,
      progression,
      businessName,
      editDialogVisible,
      editProjectDialog,
      onProjectUpdated,
      project_id
    }
  }
});
</script>
