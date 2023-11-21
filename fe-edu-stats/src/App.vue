<template>
  <div id="container-app">
    <div id="title-page">
      <h1>Education Indicators</h1>
      <h2>
        Primary and secundary indicators of Colombia
      </h2>
      <div id="container-selector">
        <p>Select an indicator </p>
        <select id="selector-ind" v-model="selectedInd">
          <option v-for="ind in indicador_selected">{{ ind }}</option>
        </select>
      </div>
      <div id="container-button">
        <p>Clic to run a query </p>
        <button @click="getIndicators">Run Query</button>
      </div>
      <div id="container-results">
        <h3>Query results</h3>
        <ul>
          <li v-if="Object.keys(queryInd).length !== 0">
            Query name: {{ queryInd[0].indicator_name }}
          </li>
        </ul>
      </div>
    </div>
  </div>
  <div id="container-chart">
    <Line id="chart" v-if="loaded" :data="chartData(queryInd)" />
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js'
import { Line } from 'vue-chartjs'

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
)

// indicator chart
let loaded = false
const chartData = (data) => {
  // Transforma los datos en el formato requerido por Chart.js
  return {
    labels: data.map(item => item.indicator_year),
    datasets: [
      {
        label: data[0].indicator_name,
        borderColor: 'rgba(75,192,192,1)',
        data: data.map(item => item.indicator_value),
      },
    ],
  };
};


// Connect with backend
axios.defaults.baseURL = "http://localhost:5000";
let queryInd = ref({});
const getIndicators = () => {
  if (selectedInd === "") {
    alert("Select and indicator");
    return;
  }
  axios.get(`/indicators?indicator_name=${selectedInd}`)
    .then((res) => {
      queryInd.value = res.data;
      loaded = true
    })
    .catch((error) => {
      alert("Error in query");
    });
};

// Populate select
const indicador_selected = ref([]);
let selectedInd = "";

onMounted(() => {
  axios.get('/indicators-to-select')
    .then((res) => {
      indicador_selected.value = res.data;
    })
    .catch((error) => {
      alert("Error in query");
    });
});

</script>
