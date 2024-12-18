<template>
   <q-expansion-item
        expand-separator
        icon="folder"
        label="Projects"
        caption="My projects"
        default-opened
        class="text-accent"
    >
        <q-list>
            <q-item v-for="project in projects" :key="project.id" clickable v-ripple :to="`/home/${store.uid}/project/${project.id}`">
              <q-item-section>
                    <q-item-label class="text-accent">{{ project.name }}</q-item-label>
                </q-item-section>
                <q-item-section side>
                    <q-badge :style="{ background: getProgressGradient(project.progress) }" :label="`${project.progress}%`" />                
                </q-item-section>
                <q-item-section side v-if="project.role_perm >= 63">
                    <q-btn flat round color="negative" icon="close" @click.stop="confirmDelete(project.id)">
                        <q-tooltip>Delete project</q-tooltip>
                    </q-btn>
                </q-item-section>
            </q-item>
        </q-list>


        <q-item clickable v-ripple to="/new/project">
            <q-item-section avatar>
                <q-icon class="text-positive" name="add" color="primary" />
            </q-item-section>
            <q-item-section class="text-positive">New project</q-item-section>
        </q-item>

    </q-expansion-item>

    <q-dialog v-model="confirmDeleteDialog">
      <q-card>
        <q-card-section class="row items-center">
          <span class="q-ml-sm">Are you sure you want to delete this project?</span>
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="Cancel" color="warning" v-close-popup />
          <q-btn flat label="Delete" color="negative" @click="deleteProject" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>
</template>

<script>
import { ref, onMounted } from 'vue'
import { apiGet, apiDelete } from '../utils/api-wrapper'
import { useUserStore } from 'stores/user-store'

export default {
  name: 'ProjectsItem',
  setup() {
    const projects = ref([])
    const store = useUserStore()
    const confirmDeleteDialog = ref(false)
    const projectToDelete = ref(null)

    const fetchProjects = async () => {
      try {
        const response = await apiGet('/user/'+`${store.uid}`+'/projects/')    
        projects.value = response
        store.setProjects(response)
      } catch (error) {
        console.error('Error fetching projects:', error)
      }
    }

    const confirmDelete = (projectId) => {
      projectToDelete.value = projectId
      confirmDeleteDialog.value = true
    }

    const deleteProject = async () => {
      try {
        await apiDelete(`/remove/project/${projectToDelete.value}/`)
        await fetchProjects()
      } catch (error) {
        console.error('Error deleting project:', error)
      }
    }

    const getProgressGradient = (progress) => {
      let color
      if (progress >= 75 && progress <= 100) {
        color = '#66754b' // Positive color
      } else if (progress >= 50 && progress < 75) {
        color = '#E9A178' // Warning color
      } else {
        color = '#C45D4E' // Negative color
      }
      return color;
    }

    onMounted(fetchProjects)

    return {
      store,
      projects,
      confirmDeleteDialog,
      confirmDelete,
      deleteProject,
      getProgressGradient
    }
  }
}
</script>

<style scoped>
.q-item {
  border-radius: 8px;
  margin-bottom: 4px;
}
</style>
