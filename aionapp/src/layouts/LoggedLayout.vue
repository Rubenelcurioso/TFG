<template>
    <q-layout view="hHh LpR lFf">
      <q-header bordered class="bg-secondary text-black">
        <q-toolbar>
          <DrawerButton @toggle-drawer="toggleDrawer" />
  
          <q-toolbar-title class="text-center">        
          </q-toolbar-title>
          <NotificationBell />
          <AvatarMenu />
        </q-toolbar>
      </q-header>
  
      <MainDrawer v-model="leftDrawerOpen" />
  
      <q-page-container>
        <router-view />
      </q-page-container>
    </q-layout>
  </template>
  
  <script>
  import { ref } from 'vue'
  import DrawerButton from 'components/DrawerButton.vue'
  import MainDrawer from 'components/MainDrawer.vue'
  import NotificationBell from 'components/NotificationBell.vue'
  import AvatarMenu from 'components/AvatarMenu.vue'
  
  export default {
    components: {
      DrawerButton,
      MainDrawer,
      NotificationBell,
      AvatarMenu
    },
    setup() {
      const leftDrawerOpen = ref(false)
  
      const toggleDrawer = () => {
        leftDrawerOpen.value = !leftDrawerOpen.value
      }
  
      return {
        leftDrawerOpen,
        toggleDrawer
      }
    }
  }
  </script>