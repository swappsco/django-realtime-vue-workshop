<template>
  <div class="small">
    <pie-chart :chart-data="datacollection" v-if="datacollection"></pie-chart>
  </div>
</template>

<script>
import PieChart from "./PieChart.js";

export default {
  components: {
    PieChart
  },
  props: { results: Object },
  data() {
    return {
      datacollection: null,
      item_colors: []
    };
  },
  mounted() {
    this.drawChart();
  },
  methods: {
    drawChart() {
      this.datacollection = {
        labels: Object.keys(this.results),
        datasets: [
          {
            label: "Results Experiment",
            backgroundColor: this.item_colors,
            data: Object.values(this.results)
          }
        ]
      };
    },
    dynamicColors: function() {
      var r = Math.floor(Math.random() * 255);
      var g = Math.floor(Math.random() * 255);
      var b = Math.floor(Math.random() * 255);
      return "rgb(" + r + "," + g + "," + b + ")";
    },
    addColor: function() {
      this.item_colors.push(this.dynamicColors());
    }
  }
};
</script>
