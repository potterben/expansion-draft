<template>
    <b-container v-if="playerData">
        <h3>
            {{positionTitle}}
        </h3>
        <b-table striped outlined responsive sticky-header :fields="getCurrentTableColumns" :items="getCurrentTeamPlayerTableData">
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
                    "key": "protect"
                },
                {
                    "key": "expose"
                },
                {
                    "key": "name",
                    "sortable": true
                },
                {
                    "key": "age",
                    "sortable": true
                },
                {
                    "key": "position",
                    "sortable": true
                },
                {
                    "key": this.currFinancialMetric,
                    "label": this.getCurrFinancialMetricText,
                    "sortable": true,
                    "formatter" : "formatFinancialMetric"
                },
                {
                    "key": this.currPerformanceMetric,
                    "label":this.getCurrPerformanceMetricText,
                    "sortable": true,
                    "formatter" : "formatPerformanceMetric"
                },
                {
                    "key": "expiry",
                    "sortable": true
                },
                {
                    "key": "meets_req",
                    "label": "Meets Exposure Requirements",
                    "sortable": true,
                    "formatter" : "formatMeetsRequirements"
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
.outline {
    outline: 3px solid #EE0000;
}
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
