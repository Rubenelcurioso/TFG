<template>
  <q-header elevated class="bg-primary text-black">
    <q-toolbar>
      <q-toolbar-title>
          <q-img src="icons/aion.png" to="/" alt="Logo" style="width: 10%; height: auto;" />       
      </q-toolbar-title>
      <q-space />
      <q-btn flat label="Home" to="/home" />
      <q-btn flat label="Solutions" />
      <q-btn flat label="Resources" />
      <q-btn flat label="Contact" />
      <q-btn outline label="Sign in" class="q-mr-sm" to="/login" />
      <q-btn color="secondary" label="Register" to="/register" />
    </q-toolbar>
  </q-header>
</template>

<script>
export default {
  name: 'LandHeader'
}
</script>