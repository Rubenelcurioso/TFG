<template>
  <q-page class="q-pa-md">
    <h1>{{ projectName }}</h1>

    <q-tabs
      v-model="tab"
      class="text-teal"
      align="left"
    >
      <q-tab name="tasks" label="Tasks" />
      <q-tab name="properties" label="Properties" />
    </q-tabs>

    <q-tab-panels v-model="tab" animated>
      <q-tab-panel name="tasks">
        <q-table
          :rows="tasks"
          :columns="columns"
          row-key="id"
          :v-model="pagination"
        >
          <template v-slot:body="props">
            <q-tr :props="props">
              <q-td key="name" :props="props">
                {{ props.row.name }}
              </q-td>
              <q-td key="assignee" :props="props">
                {{ props.row.assignee }}
              </q-td>
              <q-td key="dueDate" :props="props">
                {{ props.row.dueDate }}
              </q-td>
              <q-td key="status" :props="props">
                {{ props.row.status }}
              </q-td>
            </q-tr>
          </template>
        </q-table>
      </q-tab-panel>

      <q-tab-panel name="properties">
        <div class="text-h6">Project Properties</div>
        <p>Project ID: {{ projectId }}</p>
        <p>Created At: {{ createdAt }}</p>
        <p>Owner: {{ owner }}</p>
      </q-tab-panel>
    </q-tab-panels>
  </q-page>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'ProjectPage',
  setup() {
    const tab = ref('tasks')
    const projectName = ref('My Asana Project')
    const projectId = ref('123456')
    const createdAt = ref('2023-05-01')
    const owner = ref('John Doe')

    const tasks = ref([
      {
        id: 1,
        name: 'Task 1',
        assignee: 'Alice',
        dueDate: '2023-05-15',
        status: 'In Progress'
      },
      {
        id: 2,
        name: 'Task 2',
        assignee: 'Bob',
        dueDate: '2023-05-20',
        status: 'Not Started'
      },
      // Add more tasks as needed
    ])

    const columns = [
      { name: 'name', required: true, label: 'Task Name', align: 'left', field: 'name' },
      { name: 'assignee', required: true, label: 'Assignee', align: 'left', field: 'assignee' },
      { name: 'dueDate', required: true, label: 'Due Date', align: 'left', field: 'dueDate' },
      { name: 'status', required: true, label: 'Status', align: 'left', field: 'status' }
    ]

    const pagination = ref({
      sortBy: 'name',
      descending: false,
      page: 1,
      rowsPerPage: 10
    })

    return {
      tab,
      projectName,
      projectId,
      createdAt,
      owner,
      tasks,
      columns,
      pagination
    }
  }
}
</script>
