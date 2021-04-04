<template>
    <b-container v-if="playerData">
        <h3>
            {{positionTitle}}
        </h3>
        <b-table striped outlined responsive sticky-header :fields="getCurrentTableColumns" :items="getCurrentTeamPlayerTableData">
            <template #cell(protect)="row">
                <b-form-checkbox :checked="row.item.protected" @change="protectionChanged"></b-form-checkbox>
            </template>
            <template #cell(expose)="row">
                <b-form-checkbox :checked="row.item.exposed" @change="exposureChanged"/>
            </template>
        </b-table>
    </b-container>
</template>

<script>
import { mapState, mapGetters } from 'vuex'

export default {
    name: 'PlayerTable',

    props: {
        positionTitle: String,
        positionId: String
    },

    computed: {
        getCurrentTeamPlayerTableData() {
            let teamTableData = this.getCurrentTeamTableData;
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
                    "sortable": true
                },
                {
                    "key": "expose",
                    "sortable": true
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
        },
        ...mapState([
            'currFinancialMetric',
            'currPerformanceMetric',
            'playerData'
        ]),
        ...mapGetters([
            'getCurrentTeamTableData',
            'getCurrFinancialMetricText',
            'getCurrPerformanceMetricText'
        ])        
    },

    methods: {
        protectionChanged(value) {
            console.log("Protection changed!!")
            console.log(value)
        },
        exposureChanged(value) {
            console.log("Exposure changged!!")
            console.log(value)
        },
        formatFinancialMetric(value) {
            return "$" + value.toFixed(3) + "M";
        },
        formatPerformanceMetric(value) {
            return value.toFixed(2);
        },
        formatMeetsRequirements(value) {
            return value ? "Yes" : "No";
        },

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
