<template>
    <q-btn flat round>
      <q-avatar size="26px">
        <img src="path/to/user-avatar.png" alt="Profile">
      </q-avatar>
      <q-menu>
        <q-list style="min-width: 150px">
          <q-item clickable v-close-popup @click="openSettings">
            <q-item-section>Settings</q-item-section>
          </q-item>
          <q-item clickable v-close-popup @click="logout">
            <q-item-section>Log out</q-item-section>
          </q-item>
        </q-list>
      </q-menu>
    </q-btn>
  </template>
  
  <script>
 import { useQuasar } from 'quasar'
 import { useRouter } from 'vue-router'
 import { api } from 'boot/axios'
  export default {
    name: 'AvatarMenu',
    setup() {
      const openSettings = () => {
        // Implement settings logic here
        console.log('Opening settings')
      }

      const $q = useQuasar()
      const router = useRouter()

      const logout = () => {
        const rTkn = $q.cookies.get('rTkn')
        api.post('/logout/', { refreshToken: rTkn })
          .then(() => {
            localStorage.user = ''
            router.push('/login')
          })
          .catch(err => {
            console.error('Error logging out:', err)
          })

      }
  
      return {
        openSettings,
        logout
      }
    }
  }
  </script>