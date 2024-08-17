<template>
  <div class="q-pa-md">
    <q-table    
      flat bordered
      title="Tasks"
      :rows="rows"
      :columns="columns"
      row-key="name"
      :selected-rows-label="getSelectedString"
      selection="multiple"
      v-model:selected="selected"
    >
    
    <template v-slot:top>
      <q-btn icon="add" color="positive" @click="showDialog" label="New task" class="q-mr-sm" />
      <q-btn icon="delete" color="negative" @click="removeSelectedRows" label="Remove selected" :disable="!selected.length" />
    </template>
    
    <template v-slot:body="props">
      <q-tr :props="props">
        <q-td auto-width>
          <q-checkbox v-model="props.selected" />
        </q-td>
        <q-td v-for="col in props.cols" :key="col.name" :props="props">
          <q-input v-model="props.row[col.name]" dense borderless />
        </q-td>
      </q-tr>
    </template>

    </q-table>

    <q-dialog v-model="dialogVisible">
      <TaskCreationCard />
    </q-dialog>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue'
import TaskCreationCard from 'components/TaskCreationCard.vue'

const columns = [
        {
          name: 'name',
          required: true,
          label: 'Task name',
          align: 'left',
          field: row => row.name,
          format: val => `${val}`,
        },
        { name: 'user', align: 'center', label: 'Assigned to', field: 'user', sortable: true },
        { name: 'start_date', label: 'Starts', field: 'start', sortable: true },
        { name: 'end_date', label: 'Ends', field: 'end', sortable: true },
        { name: 'priority', label: 'Priority', field: 'priority', sortable: true },
        { name: 'status', label: 'Status', field: 'status', sortable: true},
        { name: 'team', label: 'Team assigned', field: 'team', sortable: true},
]

const rows = ref([
        {
          name: 'Frozen Yogurt',
          calories: 159,
          fat: 6.0,
          carbs: 24,
          protein: 4.0,
          sodium: 87,
          calcium: '14%',
          iron: '1%'
        }
])

export default defineComponent({
  name: 'TaskTable',
  components : {
    TaskCreationCard
    },
  setup () {
    const selected = ref([])
    const dialogVisible = ref(false)
    const newTask = ref({
      name: '',
      user: '',
      start: '',
      end: '',
      priority: '',
      status: '',
      team: ''
    })

    const getSelectedString = () => {
      return selected.value.length === 0 ? '' : `${selected.value.length} record${selected.value.length > 1 ? 's' : ''} selected of ${rows.value.length}`
    }

    const showDialog = () => {
      dialogVisible.value = true
    }



    return {
      selected,
      getSelectedString,
      columns,
      rows,
      dialogVisible,
      newTask,
      showDialog,
    }
  }
});
</script>
