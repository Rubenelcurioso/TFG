<template>
    <q-card class="bg-dark text-white">
      <q-card-section>
        <div class="row items-center justify-between">
          <div class="text-h6">Proyectos</div>
          <q-select
            v-model="selectedView"
            :options="viewOptions"
            dense
            outlined
            dark
            options-dense
            style="width: 150px"
          />
        </div>
      </q-card-section>
  
      <q-separator dark />
  
      <q-card-section>
        <q-btn flat color="grey" class="q-mb-sm" icon="add" label="Crear proyecto" to="/new/project/" />
        
        <q-item v-ripple>
          <q-list>
            <q-item v-for="project in projects" :key="project.id" clickable v-ripple :to="`/home/${$q.localStorage.getItem('user')}/project/${project.id}`">
              <q-item-section avatar>
                <q-avatar color="teal" text-color="white" icon="folder" />
              </q-item-section>
              <q-item-section>
                <q-item-label>{{ project.name }}</q-item-label>
                <q-item-label caption>{{ project.description }}</q-item-label>
              </q-item-section>
            </q-item>
          </q-list>        
        </q-item>
      </q-card-section>
    </q-card>
  </template>
  
<script>
  import { defineComponent, ref, onMounted } from 'vue';
  import { useQuasar } from 'quasar'
  import { apiGet } from '../utils/api-wrapper'
  
  export default defineComponent({
    name: 'ProjectList',
    setup() {
      const selectedView = ref('Recientes');
      const viewOptions = ['Recientes', 'Todos', 'Archivados'];
      const projects = ref([]);
      const $q = useQuasar();

      const fetchProjects = async () => {
        try {
          const response = await apiGet('/user/' + $q.localStorage.getItem('user') + '/projects/');
          projects.value = response;
        } catch (error) {
          console.error('Error fetching projects:', error);
        }
      };

      onMounted(fetchProjects);

      return {
        selectedView,
        viewOptions,
        projects,
      };
    },
  });
</script>