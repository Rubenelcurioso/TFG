<template>
  <q-page class="bg-primary q-pa-md">
    <HeroSection />
    <ImageSection />
    <q-separator/>
    <HelpUsSection />
  </q-page>
</template>

<script>
import HeroSection from 'components/HeroSection.vue'
import ImageSection from 'components/ImageSection.vue'
import HelpUsSection from 'components/HelpUsSection.vue'

export default {
  name: 'HomePage',
  components: {
    HeroSection,
    ImageSection,
    HelpUsSection
  }
}
</script>