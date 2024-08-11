<template>
    <q-page class="q-pa-md bg-accent">
      <div class="row q-col-gutter-md">
        <div class="col-12 col-md-6">
          <TaskList title="Mis tareas" />
        </div>
        <div class="col-12 col-md-6">
          <TaskList title="Tareas de equipo" />
        </div>
      </div>
      
      <div class="row q-col-gutter-md q-mt-md">
        <div class="col-12 col-md-6">
          <ProjectList />
        </div>
        <div class="col-12 col-md-6">
          <TaskTeamList />
        </div>
      </div>
    </q-page>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  import TaskList from 'components/TaskList.vue';
  import ProjectList from 'components/ProjectList.vue';
  import TaskTeamList from 'components/TaskTeamList.vue';
  
  export default defineComponent({
    name: 'HomeUser',
    components: {
      TaskList,
      ProjectList,
      TaskTeamList,
    },
  });
  </script>