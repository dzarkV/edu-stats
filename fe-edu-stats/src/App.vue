<template>
  <div id="app">
    <h1>Education Indicators</h1>
  </div>
  <div>
      <p>Clic to run a query </p>
      <button @click="getIndicators">Run Query</button>
   </div>
    <h2>
      Primary and secundary indicators of Colombia
    </h2>
    <div>
      <p>Select an indicator </p>
      <select v-model="selectedInd">
        <option v-for="ind in indicador_selected">{{ ind }}</option>
      </select>
    </div>
  <div>
    <h3>Query results</h3>
    <ul>
      <li v-if="Object.keys(queryInd).length !== 0">
        {{ queryInd[0].indicator_name}}
      </li>
    </ul>
    <!-- <ul>
      <li v-for="item in queryInd" :key="item.id">
        {{ item }}
      </li>
    </ul> -->
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
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
        })
        .catch((error) => {
          console.error(error);
        });
    };

const indicador_selected = ref([]);
let selectedInd = "";

onMounted( () =>  {
      axios.get('/indicators-to-select')
        .then((res) => {
          indicador_selected.value = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    });

  
</script>

