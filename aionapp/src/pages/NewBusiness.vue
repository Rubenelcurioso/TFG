<template>
  <q-page class="flex flex-center">
    <q-stepper
      v-model="step"
      color="primary"
      animated
    >
      <q-step
        :name="1"
        title="Business details"
        icon="business"
        :done="step > 1"
      >
        <q-input v-model="businessName" label="Business name" :rules="[
          val => val && val.length > 0 || 'Company name is required',
          val => val.length <= 255 || 'Company name too long'
        ]" />
        <q-input v-model="businessDescription" type="textarea" label="Business description" />
        <q-input v-model="businessEmail" type="email" label="Business email" :rules="[
          val => val && val.length > 0 || 'Email is required',
          val => val.length <= 150 || 'Email too long',
          val => /^\S+@\S+\.\S+$/.test(val) || 'Email is not valid'
        ]" />
        <q-input v-model="businessLocation" label="Business location" />
        <q-input v-model="businessPhone" label="Business phone" :rules="[
          val => !val || val.length <= 20 || 'Phone number too long'
        ]" />
        
        <q-stepper-navigation>
          <q-btn @click="step = 2" color="dark" label="Next" />
        </q-stepper-navigation>
      </q-step>

      <q-step
        :name="2"
        title="Confirmation"
        icon="check"
        :done="step > 2"
      >
        <q-card>
          <q-card-section>
            <div class="text-h6">Business Details</div>
            <div><strong>Name:</strong> {{ businessName }}</div>
            <div><strong>Description:</strong> {{ businessDescription }}</div>
            <div><strong>Email:</strong> {{ businessEmail }}</div>
            <div><strong>Location:</strong> {{ businessLocation }}</div>
            <div><strong>Phone:</strong> {{ businessPhone }}</div>
          </q-card-section>
        </q-card>

        <q-stepper-navigation>
          <q-btn flat @click="step = 1" color="primary" label="Back" class="q-mr-sm" />
          <q-btn @click="createBusiness" color="primary" label="Create Business" />
        </q-stepper-navigation>
      </q-step>
    </q-stepper>
  </q-page>
</template>

<script>
import { ref } from 'vue'
import { apiPost } from '../utils/api-wrapper'
import { useUserStore } from 'stores/user-store';
import { useRouter } from 'vue-router'

export default {
  name: 'NewBusiness',
  setup() {
    const step = ref(1)
    const businessName = ref('')
    const businessDescription = ref('')
    const businessEmail = ref('')
    const businessLocation = ref('')
    const businessPhone = ref('')
    const store = useUserStore()
    const router = useRouter()

    const createBusiness = async () => {
      try {
        const businessData = {
          name: businessName.value,
          description: businessDescription.value,
          email: businessEmail.value,
          location: businessLocation.value,
          phone: businessPhone.value,
          owner: store.uid
        };

        const response = await apiPost('/new/business/', businessData);

        if (response && response.id) {
          await router.push(`/home/${store.uid}/business/${response.id}/`);
        } else {
          throw new Error('Failed to create business');
        }
      } catch (error) {
        console.error('Error creating business:', error);
        // Handle error (e.g., show error message to user)
      }
    }

    return {
      step,
      businessName,
      businessDescription,
      businessEmail,
      businessLocation,
      businessPhone,
      createBusiness
    }
  }
}
</script>
