<template>
  <q-page padding>
    <h1 class="text-h4 q-mb-md">Contact Us</h1>
    <q-form @submit="onSubmit" class="q-gutter-md">
      <q-input
        filled
        v-model="name"
        label="Your Name"
        hint="Name and surname"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Please type your name']"
      />

      <q-input
        filled
        v-model="email"
        label="Your Email"
        hint="example@email.com"
        lazy-rules
        :rules="[
          val => val && val.length > 0 || 'Please type your email',
          val => val && /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(val) || 'Please type a valid email'
        ]"
      />

      <q-input
        filled
        v-model="message"
        type="textarea"
        label="Your Message"
        hint="What would you like to tell us?"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Please type your message']"
      />

      <div>
        <q-btn label="Submit" type="submit" color="primary"/>
        <q-btn label="Reset" type="reset" color="primary" flat class="q-ml-sm" @click="onReset"/>
      </div>
    </q-form>
  </q-page>
</template>

<script>
import { ref } from 'vue'
import { useQuasar } from 'quasar'

export default {
  name: 'ContactPage',
  setup () {
    const $q = useQuasar()

    const name = ref('')
    const email = ref('')
    const message = ref('')

    const onSubmit = () => {
      $q.notify({
        color: 'green-4',
        textColor: 'white',
        icon: 'cloud_done',
        message: 'Submitted'
      })
    }

    const onReset = () => {
      name.value = null
      email.value = null
      message.value = null
    }

    return {
      name,
      email,
      message,
      onSubmit,
      onReset
    }
  }
}
</script>
