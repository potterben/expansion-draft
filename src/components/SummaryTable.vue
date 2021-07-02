<template>
    <b-container v-if="expansionTeam && expansionTeam.selected" class="py-4">
        <b-row class="col-12 justify-content-center"> 
            <h3 class="capitalize">
                Summary
            </h3>
        </b-row>
        <b-table
        :fields="getSummaryTableColumns"
        :items="getSummaryTableData"
        hover
        outlined
        responsive
        class="text-nowrap"
        />
    </b-container>
</template>

<script>
import { mapGetters, mapState} from 'vuex'

export default {
    name: 'SummaryTable',

    computed: {
        ...mapState([
            'currFinancialMetric',
            'currPerformanceMetric',
            'expansionTeam'
        ]),
        ...mapGetters([
            'getSummaryTableData',
            'getCurrFinancialMetricText',
            'getCurrPerformanceMetricText'
        ]),
        getSummaryTableColumns() {
            return [
                {
                    "key": "rowname",
                    "label": "Position",
                    "sortable": true,
                    "thClass": "table-header text-wrap"
                },
                {
                    "key": "age",
                    "sortable": true,
                    "formatter" : "formatAverageAge",
                    "thClass": "table-header text-wrap"
                },
                {
                    "key": this.currFinancialMetric,
                    "label": this.getCurrFinancialMetricText,
                    "sortable": true,
                    "formatter" : "formatFinancialMetric",
                    "thClass": "table-header text-wrap"
                },
                {
                    "key": this.currPerformanceMetric,
                    "label":this.getCurrPerformanceMetricText,
                    "sortable": true,
                    "formatter" : "formatPerformanceMetric",
                    "thClass": "table-header text-wrap"
                }
            ];
        }
    },

    methods: {
        formatAverageAge(value) {
            return value.toFixed(1);
        },
        formatFinancialMetric(value) {
            return "$" + value.toFixed(3) + "M";
        },
        formatPerformanceMetric(value) {
            if (this.currPerformanceMetric == "ea_rating") {
                return value.toFixed(0);
            } else {
                return value.toFixed(2)
            }
        },
        formatBooleanValue(value) {
            return value ? "Yes" : "No";
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
