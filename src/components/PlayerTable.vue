<template>
    <div>
        <h3>{{position_title}}</h3>
        <table class='table table-hover table-striped table-team sticky-header'>
            <thead>
                <tr>
                    <th>Protect</th>
                    <th>Expose</th>
                    <th>Name</th>
                    <th>Age</th>
                    <th>Pos.</th>
                    <th v-for="metric in currPerformanceMetric" :key="metric.value" :class="metric.value">
                      {{metric.text}}
                    </th>
                    <th v-for="metric in currFinancialMetric" :key="metric.value" :class="metric.value">
                      {{metric.text}}
                    </th>
                    <th>Expiry</th>
                    <th>Exposure Req. Met</th>
                </tr>
            </thead>
            <tbody v-bind:id ="position_id">
            </tbody>
        </table>
        </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'PlayerTable',
  props: {
    position_title: String,
    position_id: String
  },
  inject : [
    'metrics'
  ],
  computed: {
  currPerformanceMetric: function () {
    return this.metrics.performance_metric.filter(team => team.value === this.getCurrPerformanceMetric);
    },
  currFinancialMetric: function () {
    return this.metrics.financial_metric.filter(team => team.value === this.getCurrFinancialMetric);
    },
    ...mapGetters([
      'getCurrPerformanceMetric',
      'getCurrFinancialMetric'      
    ])
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
