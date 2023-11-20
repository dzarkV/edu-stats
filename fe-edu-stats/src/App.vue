<template>
  <div id="app">
    <h1>Education Indicators</h1>
    <div class="container">
      <BarChart />
    </div>
    <div class="container">
      <Bar v-if="loaded" :data="chartData" />
    </div>
    <!-- <div class="indicator" v-for="indicator in indicators" :key="indicator.indicator_id">
        <h2>{{ indicator.indicator_name }}</h2>
        <div class="chart">
          <canvas :id="'chart-' + indicator.indicator_id"></canvas>
        </div>
      </div> -->
  </div>
</template>

<script>
import axios from "axios";
// import Chart from "chart.js";
import BarChart from './components/BarChart.vue'

// export  {
//   name: 'App',
//   components: { BarChart }
// }

import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'BarChart',
  components: { Bar },
  data: () => ({
    loaded: false,
    chartData: null
  }),
  async mounted() {
    this.loaded = false

    try {
      const { indicatorslist } = await axios.get('http://0.0.0.0:8000').then((response) => { this.indicators = response.data })
      this.chartData = indicatorslist
      console.log(this.chartData)
      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  }
}
</script>

