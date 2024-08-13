<template>
   <q-expansion-item
        expand-separator
        icon="folder"
        label="Projects"
        caption="My projects"
        default-opened
    >
        <q-list>
            <q-item v-for="project in projects" :key="project.id" clickable v-ripple>
                <q-item-section>
                    <q-item-label>{{ project.name }}</q-item-label>
                    <q-item-label caption>{{ project.description }}</q-item-label>
                </q-item-section>
                <q-item-section side>
                    <q-badge color="primary" :label="project.tasksCount" />
                </q-item-section>
            </q-item>
        </q-list>


        <q-item clickable v-ripple>
            <q-item-section avatar>
                <q-icon name="add" color="primary" />
            </q-item-section>
            <q-item-section>New project</q-item-section>
        </q-item>

    </q-expansion-item>
</template>

<script>
import { ref, onMounted } from 'vue'
import { apiGet } from '../utils/api-wrapper'
import { useQuasar } from 'quasar'

export default {
  name: 'ProjectsItem',
  setup() {
    const projects = ref([])


    const fetchProjects = async () => {
      const $q = useQuasar()
      try {
        const response = await apiGet('/user/'+`${$q.localStorage.getItem('user')}`+'/projects/')
        projects.value = response
      } catch (error) {
        console.error('Error fetching projects:', error)
      }
    }

    onMounted(fetchProjects)

    return {
      projects
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
