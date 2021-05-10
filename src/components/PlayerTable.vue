<template>
    <b-container v-if="playerData" class="py-4">
        <b-row class="py-2 col-12 justify-content-center"> 
            <h3>
                {{positionTitle}}
            </h3>
        </b-row>
        <b-table
        :fields="getCurrentTableColumns"
        :items="getCurrentTeamPlayerTableData"
        outlined
        responsive
        class ="text-nowrap"
        >
            <template #cell(protect)="row">
                <ProtectedCheckbox :id="row.item._id" :positionId="positionId" />
            </template>
            <template #cell(expose)="row">
                <ExposedCheckbox :id="row.item._id" :positionId="positionId" />
            </template>
        </b-table>
    </b-container>
</template>

<script>
import ProtectedCheckbox from './ProtectedCheckbox.vue'
import ExposedCheckbox from './ExposedCheckbox.vue'

import { mapGetters, mapState } from 'vuex'

export default {
    name: 'PlayerTable',

    components: {
        ProtectedCheckbox,
        ExposedCheckbox
    },

    props: {
        positionTitle: String,
        positionId: String
    },

    computed: {
        ...mapState([
            'currFinancialMetric',
            'currPerformanceMetric',
            'playerData'
        ]),
        ...mapGetters([
            'getCurrTeamTableData',
            'getCurrFinancialMetricText',
            'getCurrPerformanceMetricText'
        ]),
        getCurrentTeamPlayerTableData() {
            let teamTableData = this.getCurrTeamTableData;
            if (teamTableData) {
                return teamTableData[this.positionId];
            }
            else {
                return []
            }
        },
        getCurrentTableColumns() {
            return [
                {
                    "key": "protect",
                    "tdClass": "table-row",
                    "thClass": "table-header"
                },
                {
                    "key": "expose",
                    "tdClass": "table-row",
                    "thClass": "table-header"
                },
                {
                    "key": "name",
                    "sortable": true,
                    "tdClass": "table-row",
                    "thClass": "table-header"
                },
                {
                    "key": "age",
                    "sortable": true,
                    "tdClass": "table-row",
                    "thClass": "table-header"
                },
                {
                    "key": "position",
                    "sortable": true,
                    "tdClass": "table-row",
                    "thClass": "table-header"
                },
                {
                    "key": this.currFinancialMetric,
                    "label": this.getCurrFinancialMetricText,
                    "sortable": true,
                    "formatter" : "formatFinancialMetric",
                    "tdClass": "table-row",
                    "thClass": "table-header"
                },
                {
                    "key": this.currPerformanceMetric,
                    "label":this.getCurrPerformanceMetricText,
                    "sortable": true,
                    "formatter" : "formatPerformanceMetric",
                    "tdClass": "table-row",
                    "thClass": "table-header"
                },
                {
                    "key": "expiry",
                    "sortable": true,
                    "tdClass": "table-row",
                    "thClass": "table-header"
                },
                {
                    "key": "meets_req",
                    "label": "Meets Exposure Requirements",
                    "sortable": true,
                    "formatter" : "formatMeetsRequirements",
                    "tdClass": "table-row",
                    "thClass": "table-header"
                }
            ];
        }      
    },

    methods: {
        formatFinancialMetric(value) {
            return "$" + value.toFixed(3) + "M";
        },
        formatPerformanceMetric(value) {
            return value.toFixed(2);
        },
        formatMeetsRequirements(value) {
            return value ? "Yes" : "No";
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
