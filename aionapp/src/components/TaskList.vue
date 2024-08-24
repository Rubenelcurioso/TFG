<template>
  <q-card class="bg-dark text-white">
    <q-card-section>
      <div class="text-h6">{{ title }}</div>
    </q-card-section>

    <q-separator dark />

    <q-card-section>
      <q-table
        flat
        bordered
        dark
        :rows="tasks"
        :columns="columns"
        row-key="id"
        :filter="filter"
      >
        <template v-slot:top-right>
          <q-input dark dense debounce="300" v-model="filter" placeholder="Search">
            <template v-slot:append>
              <q-icon name="search" />
            </template>
          </q-input>
        </template>

        <template v-slot:body="props">
          <q-tr :props="props">
            <q-td v-for="col in props.cols" :key="col.name" :props="props">
              {{ col.name === 'start_date' || col.name === 'end_date' ? formatDate(props.row[col.field]) : props.row[col.field] }}
            </q-td>
          </q-tr>
        </template>
      </q-table>
    </q-card-section>
  </q-card>
</template>

<script>
import { defineComponent, onMounted, ref } from 'vue';
import { apiGet } from '../utils/api-wrapper'
import { useUserStore } from 'stores/user-store';
import { date } from 'quasar'

export default defineComponent({
  name: 'TaskList',
  props: {
    title: {
      type: String,
      required: true,
    },
    team: {
      type: Boolean,
      required: true,
    },
  },
  setup(props) {
    const store = useUserStore();
    const filter = ref('');
    const columns = [
        {
          name: 'name',
          required: true,
          label: 'Task name',
          align: 'left',
          field: 'name',
          format: val => `${val}`,
        },
        { name: 'start_date', label: 'Starts', field: 'start_date', sortable: true },
        { name: 'end_date', label: 'Ends', field: 'end_date', sortable: true },
        { name: 'priority', label: 'Priority', field: 'priority', sortable: true },
        { name: 'status', label: 'Status', field: 'status', sortable: true},
        { name: 'team', label: 'Team assigned', field: 'team', sortable: true},
    ];
    const tasks = ref([]);

    const fetchTasks = async () => {
          try {
            let response;
            if(!props.team)
              response = await apiGet(`/user/${store.uid}/tasks/`);
            else
              response = await apiGet(`/user/${store.uid}/team/tasks/`);
                       
            tasks.value = response;
          } catch (error) {
            console.error('Error fetching tasks:', error);
            // Handle the error appropriately, e.g., show an error message to the user
          }     
    };

    const formatDate = (dateString) => {
      if (!dateString) return '';
      return date.formatDate(dateString, 'YYYY-MM-DD');
    };

    onMounted(() => {
      fetchTasks();
    });

    return {
      filter,
      columns,
      tasks,
      formatDate,
    };
  },
});
</script>