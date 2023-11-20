<template>
  <div id="app">
    <h1>Education Indicators</h1>
    <p>Aqui está el mensaje: {{ msg }}</p>
    <!-- <div class="container">
      <BarChart />
    </div>
    <div class="container">
      <Bar v-if="loaded" :data="chartData" />
      {{ chartData }}
    </div> -->
    <!-- <div class="indicator" v-for="indicator in indicators" :key="indicator.indicator_id">
        <h2>{{ indicator.indicator_name }}</h2>
        <div class="chart">
          <canvas :id="'chart-' + indicator.indicator_id"></canvas>
        </div>
      </div> -->
  </div>
</template>

<script setup>
import axios from "axios";
const msg = []
const getMesagge = () => {
      axios.get('/')
        .then((res) => {
          msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    };
// // import Chart from "chart.js";
// import BarChart from './components/BarChart.vue'

// import { Bar } from 'vue-chartjs'
// import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

// ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

//     loaded = true

//     chartData = {
//       labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
//       datasets: [
//         {
//           label: 'Data One',
//           backgroundColor: '#f87979',
//           data: [40, 20, 30, 50, 60, 70, 80]
//         }
//       ]
//     }

    // try {
    //   const { indicatorslist } = await axios.get('http://0.0.0.0:8000').then((response) => { this.indicators = response.data })
    //   this.chartData = indicatorslist
    //   console.log(this.chartData)
    //   this.loaded = true
    // } catch (e) {
    //   console.error(e)
    // }


</script>

