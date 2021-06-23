<template>
    <b-container v-if="getExpansionTeamPlayerData" class="py-4">
        <b-row class="py-2 col-12 justify-content-center"> 
            <h3 class="capitalize">
                {{position}}
            </h3>
        </b-row>
        <b-table
        :fields="getExpansionTableColumns"
        :items="getExpansionTeamPlayerData"
        hover
        outlined
        responsive
        class="text-nowrap"
        >
            <template #cell(keep)="row">
                <TableCheckbox
                :id="row.item.id"
                :position="position"
                :checkedMap="expansionTeamKeepMap"
                />
            </template>
            <template #cell(remove)="row">
                <TableCheckbox
                :id="row.item.id"
                :position="position"
                :checkedMap="expansionTeamRemoveMap"
                />
            </template>
        </b-table>
    </b-container>
</template>

<script>
import TableCheckbox from './TableCheckbox.vue'

import { mapGetters, mapState, mapActions } from 'vuex'

export default {
    name: 'ExpansionPlayerTable',

    components: {
        TableCheckbox
    },

    props: {
        position: String
    },

    computed: {
        ...mapState([
            'currFinancialMetric',
            'currPerformanceMetric',
            'expansionTeam',
            'forwardsString',
            'defensemenString',
            'goaliesString',
        ]),
        ...mapGetters([
            'getCurrFinancialMetricText',
            'getCurrPerformanceMetricText',
            'getExpansionTeamSelected',
            'getForwardsString',
            'getDefensemenString',
            'getGoaliesString'
        ]),
        getExpansionTeamPlayerData() {
            let expansionTeamPlayerData = this.getExpansionTeamSelected;
            if (expansionTeamPlayerData) {
                return expansionTeamPlayerData[this.position];
            }
            else {
                return [];
            }
        },
        getExpansionTableColumns() {
            return [
                {
                    "key": "keep",
                    "thClass": "table-header text-wrap"
                },
                {
                    "key": "remove",
                    "thClass": "table-header text-wrap"
                },
                {
                    "key": "name",
                    "sortable": true,
                    "thClass": "table-header text-wrap"
                },
                {
                    "key": "team",
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
                }
            ];
        },
        expansionTeamKeepMap() {
            if (this.expansionTeam && this.expansionTeam.keep) {
                return this.expansionTeam.keep;                
            }
            else {
                return {};
            }
        },
        expansionTeamRemoveMap() {
            if (this.expansionTeam && this.expansionTeam.remove) {
                return this.expansionTeam.keep;                
            }
            else {
                return {};
            }
        }
    },

    methods: {
        ...mapActions([
            'addToCurrTeamProtectedMap',
            'addToCurrTeamExposedMap',
            'removeFromCurrTeamProtectedMap',
            'removeFromCurrTeamExposedMap'
        ]),
        formatFinancialMetric(value) {
            return "$" + value.toFixed(3) + "M";
        },
        formatPerformanceMetric(value) {
            if (this.currPerformanceMetric == "ea_rating") {
                return value.toFixed(0);
            } else {
                return value.toFixed(2)
            }
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
