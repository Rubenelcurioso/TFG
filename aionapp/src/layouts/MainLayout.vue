<template>
  <q-layout view="hHh lpR fFf">
    <LandHeader />
    <q-page-container>
      <router-view />
    </q-page-container>
    <MainFooter />
  </q-layout>
</template>

<script>
import LandHeader from 'components/LandHeader.vue'
import MainFooter from 'components/MainFooter.vue'

export default {
  name: 'MainLayout',
  components: {
    LandHeader,
    MainFooter
  }
}
</script>