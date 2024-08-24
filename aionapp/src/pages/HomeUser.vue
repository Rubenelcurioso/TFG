<template>
    <q-page class="q-pa-md bg-accent">
      <div class="row q-col-gutter-md">
        <div class="col-12 col-md-6">
          <TaskList :team="false" title="Mis tareas" />
        </div>
        <div class="col-12 col-md-6">
          <TaskList :team="true" title="Tareas de equipo" />
        </div>
      </div>
      
      <div class="row q-col-gutter-md q-mt-md">
        <div class="col-12 col-md-6">
          <ProjectList />
        </div>
        <div class="col-12 col-md-6">
          <TeamList />
        </div>
      </div>
    </q-page>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  import TaskList from 'components/TaskList.vue';
  import ProjectList from 'components/ProjectList.vue';
  import TeamList from 'components/TeamList.vue';
  
  export default defineComponent({
    name: 'HomeUser',
    components: {
      TaskList,
      ProjectList,
      TeamList,
    },
    setup() {
      return {
      };
    },
  });
  </script>