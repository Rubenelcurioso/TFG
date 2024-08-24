<template>
  <q-card class="bg-grey text-white">
    <q-card-section>
      <div class="row items-center justify-between">
        <div class="text-h6">My projects</div>
      </div>
    </q-card-section>

    <q-separator dark />

    <q-card-section>
      <q-btn flat color="white" class="q-mb-sm" icon="add" label="Crear proyecto" to="/new/project/" />
      
      <q-list class="bg-white">
        <q-item v-for="project in store.projects" :key="project.id" clickable v-ripple :to="`/home/${store.uid}/project/${project.id}`">
          <q-item-section avatar>
            <q-avatar :color="project.color || 'teal'" text-color="white">
              <q-icon :name="project.icon || 'folder'" />
            </q-avatar>
          </q-item-section>
          <q-item-section>
            <q-item-label class="text-black">{{ project.name }}</q-item-label>
            <q-item-label caption>{{ project.description }}</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-card-section>
  </q-card>
</template>

<script>
import { defineComponent, ref } from 'vue';
import { useUserStore } from 'stores/user-store';

export default defineComponent({
  name: 'ProjectList',
  setup() {
    const selectedView = ref('Recientes');
    const store = useUserStore();

    return {
      store,
      selectedView,
    };
  },
});
</script>