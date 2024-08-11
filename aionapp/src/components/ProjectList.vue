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
        <q-btn flat color="grey" class="q-mb-sm" icon="add" label="Crear proyecto" />
        
        <q-item clickable v-ripple>
          <q-item-section avatar>
            <q-avatar color="teal" text-color="white" icon="folder" />
          </q-item-section>
          <q-item-section>
            <q-item-label>[TFG] Gestión de proyectos</q-item-label>
            <q-item-label caption>3 tareas que debes entregar pro...</q-item-label>
          </q-item-section>
        </q-item>
      </q-card-section>
    </q-card>
  </template>
  
  <script>
  import { defineComponent, ref } from 'vue';
  
  export default defineComponent({
    name: 'ProjectList',
    setup() {
      const selectedView = ref('Recientes');
      const viewOptions = ['Recientes', 'Todos', 'Archivados'];
  
      return {
        selectedView,
        viewOptions,
      };
    },
  });
  </script>