<template>
    <b-container class="py-4" v-if="this.expansionTeam && this.expansionTeam.selected">
        <b-row class="py-2 col-12 justify-content-center"> 
            <h3>
                Selected Player
            </h3>
        </b-row>
        <b-table
        :fields="getCurrentTableColumns"
        :items="getCurrTeamSelectedPlayerTableData"
        hover
        outlined
        responsive
        class="text-nowrap"
        />
    </b-container>
</template>

<script>

import { mapGetters, mapState } from 'vuex'

export default {
    name: 'SelectedPlayerTable',
    
    props: {
        teamInit: String
    },

    computed: {
        ...mapState([
            'currFinancialMetric',
            'currPerformanceMetric',
            'positionKeys',
            'expansionTeam'
        ]),
        ...mapGetters([
            'getCurrTeamTableData',
            'getCurrFinancialMetricText',
            'getCurrPerformanceMetricText',
            'getForwardsString',
            'getDefensemenString',
            'getGoaliesString',
        ]),
        getCurrTeamSelectedPlayerTableData() {
            if (this.expansionTeam && this.expansionTeam.selected) {
                let currSelectedPlayer = [];
                let seattleSelectedPlayers = this.expansionTeam.selected;
                this.positionKeys.forEach(positionKey => {
                    let selectedPlayers = seattleSelectedPlayers[positionKey].filter(value => value.team === this.teamInit);
                    if (selectedPlayers.length > 0) {
                        currSelectedPlayer = selectedPlayers;
                    }
                });
                return currSelectedPlayer;
            }
            else {
                return [];
            }
        },
        getCurrentTableColumns() {
            return [
                {
                    "key": "nmc",
                    "label": "NMC",
                    "sortable": true,
                    "formatter" : "formatBooleanValue",
                    "thClass": "table-header text-wrap"
                },
                {
                    "key": "name",
                    "sortable": true,
                    "thClass": "table-header text-wrap"
                },
                {
                    "key": "age",
                    "sortable": true,
                    "thClass": "table-header text-wrap"
                },
                {
                    "key": "position",
                    "sortable": true,
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
                },
                {
                    "key": "expiry",
                    "sortable": true,
                    "thClass": "table-header text-wrap"
                },
                {
                    "key": "meets_req",
                    "label": "Meets Exp. Reqs",
                    "sortable": true,
                    "formatter" : "formatBooleanValue",
                    "thClass": "table-header text-wrap"
                }
            ];
        }
    },

    methods: {
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
