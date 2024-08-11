<template>
    <q-btn
        flat
        dense
        round
        icon="menu"
        aria-label="Menu"
        @click="$emit('toggle-drawer')"
    />
</template>

<script>
    export default {
    name: 'DrawerButton',
    emits: ['toggle-drawer']
    }
</script>