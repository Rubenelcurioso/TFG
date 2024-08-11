<template>
    <q-footer reveal class="bg-secondary text-black">
      <q-toolbar>
          <img src="icons/aion.png" alt="Logo" style="width: 5%; height: auto;">
        <q-space />
      </q-toolbar>
      <q-separator />
      <div class="row q-pa-md">
        <div class="col-6 col-md-3">
          <h6 class="q-mb-md">Explore</h6>
          <q-list dense>
            <q-item clickable v-ripple><q-item-section>About us</q-item-section></q-item>
            <q-item clickable v-ripple><q-item-section>Contact</q-item-section></q-item>
          </q-list>
        </div>
        <div class="col-6 col-md-3">
          <h6 class="q-mb-md">Resources</h6>
          <q-list dense>
            <q-item clickable v-ripple><q-item-section>Privacy Politics</q-item-section></q-item>
            <q-item clickable v-ripple><q-item-section>Security</q-item-section></q-item>
            <q-item clickable v-ripple><q-item-section>Best practices</q-item-section></q-item>
          </q-list>
        </div>
      </div>
    </q-footer>
  </template>
  
  <script>
  export default {
    name: 'MainFooter'
  }
  </script>