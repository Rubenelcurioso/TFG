<template>
    <q-drawer
      :model-value="modelValue"
      @update:model-value="$emit('update:modelValue', $event)"
      show-if-above
      dark
      content-class="bg-primary"
    >
      <q-scroll-area class="fit">
          <q-list dense padding class="menu-list">
          <q-item active clickable v-ripple :to="`/home/${store.uid}`" @click="closeDrawer">            
            <q-item-section avatar>
              <q-icon name="home" />
            </q-item-section>
            <q-item-section>Home</q-item-section>
          </q-item>

          <q-separator dark spaced inset/>
          <ProjectsItem  />

          <BusinessItem />


          <q-separator dark spaced inset/>

          <q-item clickable v-ripple @click="openGithubAndCloseDrawer">
            <q-item-section avatar>
              <q-icon name="star" />
            </q-item-section>
            <q-item-section>Rate us</q-item-section>
          </q-item>

        </q-list>
      </q-scroll-area>
    </q-drawer>
  </template>
  
<script>
import ProjectsItem from 'components/ProjectsItem.vue'
import BusinessItem from 'components/BusinessItem.vue'
import { useUserStore } from 'stores/user-store'
export default {
  name: 'MainDrawer',
  components: {
    ProjectsItem,
    BusinessItem
  },
  props: {
    modelValue: {
      type: Boolean,
      required: true
    }
  },
  emits: ['update:modelValue'],
  setup() {
    const store = useUserStore();
    return { store };
  },
  methods: {
    openGithubAndCloseDrawer() {
      this.openGithub();
      this.closeDrawer();
    },
    openGithub() {
      window.open('https://github.com/Rubenelcurioso/TFG', '_blank');
    },
    closeDrawer() {
      this.$emit('update:modelValue', false);
    }
  }
}
</script>

<style lang="sass" scoped>
.menu-list .q-item
  border-radius: 0 32px 32px 0
</style>
