<template>
    <q-card class="bg-dark text-white">
      <q-card-section>
        <div class="text-h6">{{ title }}</div>
        <q-tabs
          v-model="tab"
          dense
          class="text-grey"
          active-color="white"
          indicator-color="white"
          align="left"
          narrow-indicator
        >
          <q-tab name="proximas" label="Próximas" />
          <q-tab name="conretraso" label="Con retraso (1)" />
          <q-tab name="finalizadas" label="Finalizadas" />
        </q-tabs>
      </q-card-section>
  
      <q-separator dark />
  
      <q-card-section>
        <q-btn flat color="grey" class="q-mb-sm" icon="add" label="Crear tarea" />
        
        <q-list dark>
          <q-item v-for="task in tasks" :key="task.id" clickable v-ripple>
            <q-item-section avatar>
              <q-checkbox v-model="task.done" dark color="green" />
            </q-item-section>
            <q-item-section>{{ task.title }}</q-item-section>
            <q-item-section side>
              <q-chip :color="task.chipColor" text-color="white" size="sm">
                {{ task.chipText }}
              </q-chip>
            </q-item-section>
          </q-item>
        </q-list>
        
        <div class="text-center q-mt-sm">
          <q-btn flat color="grey" label="Mostrar más" />
        </div>
      </q-card-section>
    </q-card>
  </template>
  
  <script>
  import { defineComponent, ref } from 'vue';
  
  export default defineComponent({
    name: 'TaskList',
    props: {
      title: {
        type: String,
        required: true,
      },
    },
    setup() {
      const tab = ref('proximas');
      const tasks = [
        { id: 1, title: 'Análisis de errores, riesgos, soluciones', done: false, chipColor: 'teal', chipText: '[TFG] G...' },
        { id: 2, title: 'Tests Django operaciones', done: false, chipColor: 'teal', chipText: '[TFG] S...' },
        { id: 3, title: 'Operaciones Django', done: false, chipColor: 'teal', chipText: '[TFG] G...' },
        { id: 4, title: 'Verificar contenidos .gitignore', done: false, chipColor: 'teal', chipText: '[TFG] G...' },
        { id: 5, title: '[Docker] Contenedor Django', done: false, chipColor: 'teal', chipText: '[TFG] G...' },
        { id: 6, title: '[Docker] Contenedor Nuxt', done: false, chipColor: 'teal', chipText: '[TFG] G...' },
      ];
  
      return {
        tab,
        tasks,
      };
    },
  });
  </script>