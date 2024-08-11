<template>
    <q-card class="bg-dark text-white">
      <q-card-section>
        <div class="row items-center justify-between">
          <div class="text-h6">Equipos de tareas</div>
          <q-btn flat color="grey" icon="search" label="Buscar equipos" />
        </div>
      </q-card-section>
  
      <q-separator dark />
  
      <q-card-section>
        <q-btn flat color="grey" class="q-mb-sm" icon="group_add" label="Crear equipo" />
        
        <q-list dark bordered separator>
          <q-item v-for="team in teams" :key="team.id" clickable v-ripple>
            <q-item-section avatar>
              <q-avatar :color="team.color" text-color="white">
                {{ team.initials }}
              </q-avatar>
            </q-item-section>
            <q-item-section>
              <q-item-label>{{ team.name }}</q-item-label>
              <q-item-label caption>{{ team.memberCount }} miembros</q-item-label>
            </q-item-section>
            <q-item-section side>
              <q-badge :color="team.taskColor" :label="`${team.taskCount} tareas`" />
            </q-item-section>
          </q-item>
        </q-list>
        
        <div class="text-center q-mt-sm">
          <q-btn flat color="grey" label="Ver todos los equipos" />
        </div>
      </q-card-section>
    </q-card>
  </template>
  
  <script>
  import { defineComponent, ref } from 'vue';
  
  export default defineComponent({
    name: 'TaskTeamList',
    setup() {
      const teams = ref([
        { id: 1, name: 'Desarrollo', initials: 'DE', color: 'primary', memberCount: 8, taskCount: 15, taskColor: 'orange' },
        { id: 2, name: 'Diseño', initials: 'DI', color: 'purple', memberCount: 5, taskCount: 7, taskColor: 'green' },
        { id: 3, name: 'Marketing', initials: 'MA', color: 'teal', memberCount: 6, taskCount: 10, taskColor: 'red' },
        { id: 4, name: 'Ventas', initials: 'VE', color: 'deep-orange', memberCount: 4, taskCount: 12, taskColor: 'blue' },
      ]);
  
      return {
        teams,
      };
    },
  });
  </script>