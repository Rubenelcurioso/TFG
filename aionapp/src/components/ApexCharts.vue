<template>
  <div>
    <div class="row">
      <div class="col chart-container">
        <h3 style="text-align: center;">Task priority</h3>
        <apexchart width="100%" type="donut" :options="donutChartOptions" :series="donutSeries"></apexchart>
      </div>
      <div class="col chart-container">
        <h3 style="text-align: center;">Task status</h3>
        <apexchart width="100%" type="pie" :options="pieChartOptions" :series="pieSeries"></apexchart>
      </div>
    </div>
    <div class="row">
      <div class="col chart-container">
        <h3 style="text-align: center;">Workload</h3>
        <apexchart ref="columnChart" width="100%" type="bar" :options="columnChartOptions" :series="columnSeries"></apexchart>
      </div>
    </div>
  </div>
</template>

<style scoped>
.chart-container {
  margin: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
@media (max-width: 768px) {
  .chart-container {
    margin: 5px;
    padding: 5px;
  }
}
</style>

<script>
import VueApexCharts from 'vue3-apexcharts';
import { apiGet } from '../utils/api-wrapper';
import { nextTick } from 'vue';

export default {
  name: 'ApexCharts',
  components: {
    apexchart: VueApexCharts,
  },
  props: {
    pid: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      donutSeries: [],
      donutChartOptions: {
        chart: {
          width: '100%',
          type: 'donut',
        },
        labels: ['High', 'Medium', 'Low'],
        responsive: [{
          breakpoint: 480,
          options: {
            chart: {
              width: '100%'
            },
            legend: {
              position: 'bottom'
            }
          }
        }]
      },
      columnSeries: [
        {
          name: 'Workload',
          data: []
        }
      ],
      columnChartOptions: {
        chart: {
          type: 'bar',
          height: 350
        },
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: '55%',
            endingShape: 'rounded',
            dataLabels: {
              enabled: true,
              formatter: function(val, opt) {
                return opt.w.globals.labels[opt.dataPointIndex] + ":  " + val
              },
              position: 'top',
            }
          },
        },
        stroke: {
          show: true,
          width: 2,
          colors: ['transparent']
        },
        xaxis: {
          categories: [],
        },
        fill: {
          opacity: 1
        },
        tooltip: {
          y: {
            formatter: function (val) {
              return val;
            }
          }
        }
      },
      pieSeries: [],
      pieChartOptions: {
        chart: {
          width: '100%',
          type: 'pie',
        },
        labels: ['Done', 'In progress', 'To do'],
        responsive: [{
          breakpoint: 480,
          options: {
            chart: {
              width: '100%'
            },
            legend: {
              position: 'bottom'
            }
          }
        }]
      },
    };
  },
  mounted(){
    this.getStats(this.pid);
  },
  methods: {
    async getStats(pid){
      const response = await apiGet(`/stats/${pid}/priority/`);
      this.donutSeries = [
        response.priority_counts.H || 0, 
        response.priority_counts.M || 0, 
        response.priority_counts.L || 0
      ];
      const workloadResponse = await apiGet(`/stats/${pid}/workload/`);
      console.log('Workload response:', workloadResponse);

      if (workloadResponse.workload_counts) {   
        this.columnSeries = [{
          name: 'Workload',
          data: Object.values(workloadResponse.workload_counts)
        }];
        
        this.columnChartOptions.xaxis.categories = Object.keys(workloadResponse.workload_counts);
        
        nextTick(() => {
          if (this.$refs.columnChart) {
            this.$refs.columnChart.updateOptions(this.columnChartOptions);
          }
        });
      } else {
        console.error('Workload counts not found in the response');
      }

      const statusResponse = await apiGet(`/stats/${pid}/status/`);
      this.pieSeries = [
        statusResponse.status_counts.DONE || 0, 
        statusResponse.status_counts.PENDING || 0, 
        statusResponse.status_counts.IN_PROGRESS || 0
      ];
    }
  }
};
</script>