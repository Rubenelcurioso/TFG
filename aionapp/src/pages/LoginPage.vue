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
import { useRouter } from 'vue-router'
import { apiPost } from '../utils/api-wrapper'
import { setToken, setRefreshToken } from '../utils/token-management'
import { useUserStore } from 'stores/user-store'

export default defineComponent({
  name: 'LoginPage',
  components: { AuthForm },
  setup() {
    const fields = [
      { name: 'username', label: 'Username', type: 'text' },
      { name: 'password', label: 'Password', type: 'password' }
    ]

    const errorMessage = ref('')
    const store = useUserStore()
    const router = useRouter()

    const onSubmit = async (formData) => {
      try {
        const response = await apiPost('/login/', formData)
        const { refresh, access, user, username, ts } = response
        setToken(access)
        setRefreshToken(refresh)
        store.setUser({
          uid: user,
          username: username
        })
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
