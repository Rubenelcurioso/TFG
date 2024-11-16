<template>
  <q-page class="flex flex-center bg-primary" >
    <AuthForm
      title="Registration"
      subtitle="Create your account"
      :fields="fields"
      submit-label="Register"
      v-model="formData"
      @submit="onSubmit"
    />
  </q-page>
</template>

<script>
  import { defineComponent } from 'vue'
  import AuthForm from 'components/AuthForm.vue'
  import { useRouter } from 'vue-router'
  import { apiPost } from '../utils/api-wrapper'
  import { setToken, setRefreshToken } from '../utils/token-management'
  import { useUserStore } from 'stores/user-store'
  import { useQuasar } from 'quasar'

  export default defineComponent({
    name: 'RegisterPage',
    components: { AuthForm },
    setup() {
      const fields = [
        { name: 'username', label: 'Username', rules: [
          val => val && val.length > 0 || 'Username is required',
          val => val.length <= 50 || 'Username too long',
          val => /^[a-zA-Z0-9_]+$/.test(val) || 'Username can only contain letters, numbers, and underscores'
        ]},
        { name: 'email', label: 'Email', type: 'email', rules: [
          val => val && val.length > 0 || 'Email is required',
          val => val.length <= 150 || 'Email too long',
          val => /^\S+@\S+\.\S+$/.test(val) || 'Email is not valid'
        ]},
        { name: 'fullname', label: 'Full name', rules: [
          val => val && val.length > 0 || 'Full name is required',
          val => val.length <= 255 || 'Full name too long',
          val => /^[a-zA-Z ]+$/.test(val) || 'Full name should only contain letters and spaces'
        ]},
        { name: 'birthday', label: 'Birthday', type: 'date', rules: [
          val => val && val.length > 0 || 'Birthday is required',
          val => new Date().getFullYear() - new Date(val).getFullYear() >= 14 || 'User must be at least 14 years old'
        ]},
        { name: 'password', label: 'Password', type: 'password', rules: [
          val => val && val.length > 0 || 'Password is required',
          val => val.length >= 8 || 'Password must be at least 8 characters long'
        ]},
        { name: 'password2', label: 'Confirm password', type: 'password', rules: [
          val => val && val.length > 0 || 'Password confirmation is required'
        ]},
        { name: 'phone', label: 'Phone (optional)', rules: [
          val => !val || val.length <= 20 || 'Phone number too long'
        ]}
      ]

      const router = useRouter()
      const store = useUserStore()
      const $q = useQuasar()

      const onSubmit = async (formData) => {
              try {
                const response = await apiPost('/register/', formData)
                const { refresh, access, user, username, ts } = response
                setToken(access)
                setRefreshToken(refresh)
                store.setUser({
                  uid: user,
                  username: username
                })
                $q.notify({
                  type: 'positive',
                  message: 'Registration successful!',
                  position: 'bottom-right'
                })
                router.push(`/home/${user}`)
              } catch (error) {
                console.error('Registration failed', error)
                $q.notify({
                  type: 'negative',
                  message: 'Registration failed: check the fields and try again',
                  position: 'bottom-right'
                })
              }
      }

      return { fields, onSubmit }
    }
  })
</script>