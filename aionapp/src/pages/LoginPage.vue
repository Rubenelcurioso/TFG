<template>
  <q-page class="flex flex-center bg-primary">
    <AuthForm
      title="Login"
      subtitle="Access your account"
      :fields="fields"
      submit-label="Login"
      v-model="formData"
      @submit="onSubmit"
    />
  </q-page>
</template>

<script>
import { defineComponent, ref } from 'vue'
import AuthForm from 'components/AuthForm.vue'
import { api } from 'boot/axios'
import { useQuasar } from 'quasar'
import { useRouter } from 'vue-router'

export default defineComponent({
  name: 'LoginPage',
  components: { AuthForm },
  setup() {
    const fields = [
      { name: 'username', label: 'Username', type: 'text' },
      { name: 'password', label: 'Password', type: 'password' }
    ]

    const errorMessage = ref('')

    const $q = useQuasar()
    const router = useRouter()

    const onSubmit = async (formData) => {
      try {
        const response = await api.post('/login/', formData)
        const { accessToken, refreshToken, user, ts } = response.data
        // secure cookie subject to change when adquire certifieds for HTTPS
        // NEED TO CHANGE THE OPTION ASAP have HTTPS certs
        $q.cookies.set('aTknlt', '15m', { path: '/', secure: false, httpOnly: true, sameSite: 'Strict' })
        $q.cookies.set('rTknlt', '1440m', { path: '/', secure: false, httpOnly: true, sameSite: 'Strict' })
        $q.cookies.set('rTkn', refreshToken, { path: '/', secure: false, httpOnly: true, sameSite: 'Strict' })
        $q.cookies.set('user', user, { path: '/', secure: false, httpOnly: true, sameSite: 'Strict' })
        $q.localStorage.set('ts', ts)
        $q.localStorage.set('aTkn', accessToken) 
        router.push(`/home/${user}`)    
        } catch (error) {
        console.error('Login failed', error)
        errorMessage.value = 'Login failed: ' + (error.response?.data?.message || error.message)
      }
    }

    return { fields, onSubmit, errorMessage }
  }
})
</script>
