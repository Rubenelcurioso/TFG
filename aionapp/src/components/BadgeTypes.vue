<template>
    <div class="badge-types">
       <q-badge :class="badgeColor" text-color="accent">{{ label }}</q-badge>
    </div>
</template>

<script>
export default {
    name: 'BadgeTypes',
    props: {
        label: {
            type: String,
            required: true
        }
    },
    computed: {
        badgeColor() {
            switch (this.label) {
                case 'LOW':
                    return 'low-priority';
                case 'MEDIUM':
                    return 'medium-priority';
                case 'HIGH':
                    return 'high-priority';
                case 'To do':
                    return 'todo';
                case 'In progress':
                    return 'in-progress';
                case 'Done':
                    return 'done';
                default:
                    return 'dark';
            }
        }
    }
}
</script>
