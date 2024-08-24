<template>
  <div class="q-pa-md">
    <q-table    
      flat bordered
      title="Tasks"
      :rows="rows"
      :columns="columns"
      row-key="id"
      :selected-rows-label="getSelectedString"
      selection="single"
      v-model:selected="selected"
    >
    
    <template v-slot:top>
      <q-btn icon="add" color="positive" @click="showDialog" label="New task" class="q-mr-sm" :disable="userRolePerm < 7" />
      <q-btn icon="edit" color="primary" @click="editSelectedRow" label="Edit selected" :disable="!selected.length || userRolePerm < 7" class="q-mr-sm" />
      <q-btn icon="delete" color="negative" @click="removeSelectedRows" label="Remove selected" :disable="!selected.length || userRolePerm < 7" />
    </template>
    
    <template v-slot:body="props">
      <q-tr :props="props">
        <q-td auto-width>
          <q-checkbox v-model="props.selected" />
        </q-td>
        <q-td v-for="col in props.cols" :key="col.name" :props="props">
          {{ props.row[col.field] }}
        </q-td>
      </q-tr>
    </template>

    </q-table>

    <q-dialog v-model="dialogVisible">
      <TaskCreationCard @task-created="onTaskCreate" @close-d="dialogVisible = false" />
    </q-dialog>

    <q-dialog v-model="editDialogVisible">
      <TaskEditCard :taskId="selected[0].id" @task-updated="onTaskEdit" @close-dialog="editDialogVisible = false" />    
    </q-dialog>
  </div>
</template>

<script>
import { defineComponent, ref, onMounted, watch } from 'vue'
import TaskCreationCard from 'components/TaskCreationCard.vue'
import TaskEditCard from 'components/TaskEditCard.vue'
import { apiGet, apiDelete, apiPut } from '../utils/api-wrapper'
import { useRoute } from 'vue-router'
import { useUserStore } from 'stores/user-store'

const columns = [
        {
          name: 'name',
          required: true,
          label: 'Task name',
          align: 'left',
          field: 'name',
          format: val => `${val}`,
        },
        { name: 'user', align: 'center', label: 'Assigned to', field: 'user', sortable: true },
        { name: 'start_date', label: 'Starts', field: 'start_date', sortable: true },
        { name: 'end_date', label: 'Ends', field: 'end_date', sortable: true },
        { name: 'priority', label: 'Priority', field: 'priority', sortable: true },
        { name: 'status', label: 'Status', field: 'status', sortable: true},
        { name: 'team', label: 'Team assigned', field: 'team', sortable: true},
]

export default defineComponent({
  name: 'TaskTable',
  components : {
    TaskCreationCard,
    TaskEditCard
    },
  setup () {
    const route = useRoute()
    const selected = ref([])
    const dialogVisible = ref(false)
    const editDialogVisible = ref(false)
    const rows = ref([])
    const store = useUserStore()
    const userRolePerm = ref(store.projects.find(project => project.id === parseInt(route.params.pid)).role_perm)

    const getSelectedString = () => {
      return selected.value.length === 0 ? '' : `${selected.value.length} record${selected.value.length > 1 ? 's' : ''} selected of ${rows.value.length}`
    }

    const showDialog = () => {
      dialogVisible.value = true
    }

    const fetchTasks = async () => {
      try {
        const response = await apiGet('project/'+route.params.pid+'/tasks/');
        rows.value = response;
      } catch (error) {
        console.error('Error fetching tasks:', error);
      }
    }

    const removeSelectedRows = async () => {
      try {
        for (const row of selected.value) {
          await apiDelete(`/remove/task/${row.id}/`);
        }
        await fetchTasks();
        selected.value = [];
      } catch (error) {
        console.error('Error removing tasks:', error);
      }
    }

    const editSelectedRow = () => {
      if (selected.value.length === 1) {
        editDialogVisible.value = true;
      }
    }

    const onTaskEdit = async () => {
      await fetchTasks();
      editDialogVisible.value = false;
      selected.value = [];
    }

    const onTaskCreate = async () => {
      await fetchTasks();
      dialogVisible.value = false;
    }

    onMounted(() => {
      fetchTasks()
    })

    return {
      selected,
      getSelectedString,
      columns,
      rows,
      dialogVisible,
      editDialogVisible,
      showDialog,
      removeSelectedRows,
      editSelectedRow,
      onTaskEdit,
      onTaskCreate,
      userRolePerm,
    }
  }
});
</script>