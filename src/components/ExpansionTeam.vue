<template>
    <b-container>
        <template v-if="this.figureData">
            <Figure :metricName="'Average Age'" :metric="'age'"/>
            <Figure :metricName="getCurrPerformanceMetricFigureText" :metric="currPerformanceMetric"/>
            <Figure :metricName="getCurrFinancialMetricFigureText" :metric="currFinancialMetric" :isFinancial="true"/>
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
            "getCurrFinancialMetricFigureText",
            "getCurrPerformanceMetricFigureText"
            
        ])
    }
}
</script>