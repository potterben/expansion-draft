<template>
    <b-container>
        <template v-if="this.figureData">
            <Figure :metricName="'Average Age'" :metric="'age'"/>
            <Figure :metricName="getCurrPerformanceMetricText" :metric="currPerformanceMetric"/>
            <Figure :metricName="getCurrFinancialMetricText" :metric="currFinancialMetric" :isFinancial="true"/>
        </template>
        <SummaryTable/>
        <ExpansionPlayerTable position="forwards"/>
        <ExpansionPlayerTable position="defensemen"/>
        <ExpansionPlayerTable position="goalies"/>
   </b-container>
</template>

<script>
import Figure from './Figure.vue'
import SummaryTable from './SummaryTable.vue'
import ExpansionPlayerTable from './ExpansionPlayerTable.vue'
import { mapGetters, mapState } from 'vuex'

export default {
    name: 'TeamTable',

    components: {
        SummaryTable,
        ExpansionPlayerTable,
        Figure
    },

    computed: {
        ...mapState([
            "figureData",
            "currFinancialMetric",
            "currPerformanceMetric"
        ]),
        ...mapGetters([
            "getCurrFinancialMetricText",
            "getCurrPerformanceMetricText"
            
        ])
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
