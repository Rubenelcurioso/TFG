export default {
  head: {
    title: 'Aion',
    htmlAttrs: {
      lang: 'es'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },


  css: [
    'primevue/resources/themes/saga-blue/theme.css',
    'primevue/resources/primevue.css',
    'primeicons/primeicons.css'
  ],


  plugins: [
    { src: '~/plugins/primevue.js', mode: 'client' }
  ],

  components: true,

  buildModules: [
    '@nuxtjs/tailwindcss',
  ],

  build: {
    transpile: ['primevue'],
    indicator: true
  }
}