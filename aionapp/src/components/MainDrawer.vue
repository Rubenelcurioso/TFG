<template>
    <q-drawer
      :model-value="modelValue"
      @update:model-value="$emit('update:modelValue', $event)"
      show-if-above
      bordered
      dark
      content-class="bg-primary"
    >
      <q-list>
        <q-item-label header class="text-grey-8">Navigation</q-item-label>
        <q-item clickable v-ripple>
          <q-item-section avatar>
            <q-icon name="inbox" />
          </q-item-section>
          <q-item-section>Inbox</q-item-section>
        </q-item>
        <q-item clickable v-ripple>
          <q-item-section avatar>
            <q-icon name="star" />
          </q-item-section>
          <q-item-section>Star</q-item-section>
        </q-item>
        <q-item clickable v-ripple>
          <q-item-section avatar>
            <q-icon name="send" />
          </q-item-section>
          <q-item-section>Send</q-item-section>
        </q-item>
      </q-list>
    </q-drawer>
  </template>
  
  <script>
  export default {
    name: 'MainDrawer',
    props: {
      modelValue: {
        type: Boolean,
        required: true
      }
    },
    emits: ['update:modelValue']
  }
  </script>