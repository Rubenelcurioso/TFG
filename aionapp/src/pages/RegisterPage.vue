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
  import { api } from 'boot/axios'
  import { formToJSON } from 'axios';
  import { useQuasar } from 'quasar'
  import { useRouter } from 'vue-router'

  
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

      const $q = useQuasar()
      const router = useRouter()

      const onSubmit = async (formData) => {
              try {
                const response = await api.post('/register/', formData)
                const { accessToken, refreshToken, user } = response.data
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
                console.error('Registration failed', error)
                alert('Registration failed: ' + (error.response?.data?.message || error.message))
              }
      }
  
      return { fields, onSubmit }
    }
  })
  </script>