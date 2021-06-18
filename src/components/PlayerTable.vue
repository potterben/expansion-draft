<template>
    <b-container v-if="playerData" class="py-4">
        <b-row class="py-2 col-12 justify-content-center"> 
            <h3 class="capitalize">
                {{position}}
            </h3>
        </b-row>
        <b-table
        :fields="getCurrentTableColumns"
        :items="getCurrentTeamPlayerTableData"
        hover
        outlined
        responsive
        class="text-nowrap"
        :class="isTableDisabled() ? 'disabled-table': ''"
        >
            <template #cell(protect)="row">
                <TableCheckbox
                :id="row.item.id"
                :position="position"
                :checkedMap="currTeamProtectedMap"
                :onChange="protectedChanged"
                :isTableDisabled = "isTableDisabled"
                />
            </template>
            <template #cell(expose)="row">
                <TableCheckbox
                :id="row.item.id"
                :position="position"
                :checkedMap="currTeamExposedMap"
                :onChange="exposedChanged"
                />
            </template>
        </b-table>
    </b-container>
</template>

<script>
import TableCheckbox from './TableCheckbox.vue'

import { mapGetters, mapState, mapActions } from 'vuex'

export default {
    name: 'PlayerTable',

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
            'playerData',
            'forwardsString',
            'defensemenString',
            'goaliesString'
        ]),
        ...mapGetters([
            'getCurrTeamTableData',
            'getCurrFinancialMetricText',
            'getCurrPerformanceMetricText',
            'getCurrTeamExposedMap',
            'getCurrTeamProtectedMap',
            'getForwardsString',
            'getDefensemenString',
            'getGoaliesString'
        ]),
        getCurrentTeamPlayerTableData() {
            let teamTableData = this.getCurrTeamTableData;
            if (teamTableData) {
                return teamTableData[this.position];
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
                    "thClass": "table-header text-wrap"
                },
                {
                    "key": "expose",
                    "tdClass": "table-row",
                    "thClass": "table-header text-wrap"
                },
                {
                    "key": "nmc",
                    "label": "NMC",
                    "sortable": true,
                    "formatter" : "formatBooleanValue",
                    "tdClass": "table-row",
                    "thClass": "table-header text-wrap"
                },
                {
                    "key": "name",
                    "sortable": true,
                    "tdClass": "table-row",
                    "thClass": "table-header text-wrap"
                },
                {
                    "key": "age",
                    "sortable": true,
                    "tdClass": "table-row",
                    "thClass": "table-header text-wrap"
                },
                {
                    "key": "position",
                    "sortable": true,
                    "tdClass": "table-row",
                    "thClass": "table-header text-wrap"
                },
                {
                    "key": this.currFinancialMetric,
                    "label": this.getCurrFinancialMetricText,
                    "sortable": true,
                    "formatter" : "formatFinancialMetric",
                    "tdClass": "table-row",
                    "thClass": "table-header text-wrap"
                },
                {
                    "key": this.currPerformanceMetric,
                    "label":this.getCurrPerformanceMetricText,
                    "sortable": true,
                    "formatter" : "formatPerformanceMetric",
                    "tdClass": "table-row",
                    "thClass": "table-header text-wrap"
                },
                {
                    "key": "expiry",
                    "sortable": true,
                    "tdClass": "table-row",
                    "thClass": "table-header text-wrap"
                },
                {
                    "key": "meets_req",
                    "label": "Meets Exp. Reqs",
                    "sortable": true,
                    "formatter" : "formatBooleanValue",
                    "tdClass": "table-row",
                    "thClass": "table-header text-wrap"
                }
            ];
        },
        currTeamExposedMap() {
            return this.getCurrTeamExposedMap;
        },
        currTeamProtectedMap() {
            return this.getCurrTeamProtectedMap;
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
        },
        formatBooleanValue(value) {
            return value ? "Yes" : "No";
        },
        protectedChanged(value, position, id) {
            let payload = {
                "position": position,
                "id": id
            }
            if (value) {
                this.removeFromCurrTeamExposedMap(payload);
                this.addToCurrTeamProtectedMap(payload);
            }
            else {
                this.removeFromCurrTeamProtectedMap(payload);
            }
        },
        exposedChanged(value, position, id) {
            let payload = {
                "position": position,
                "id": id
            }
            if (value) {
                this.removeFromCurrTeamProtectedMap(payload);
                this.addToCurrTeamExposedMap(payload);
            }
            else {
                this.removeFromCurrTeamExposedMap(payload);
            }
        },
        isTableDisabled() {
            if (this.getCurrTeamProtectedMap !== null) {
                switch (this.position) {
                    case "forwards":
                    case "defensemen":
                        return this.shouldTableBeDisabled(this.position);
                    case "goalies":
                        return this.shouldGoalieTableBeDisabled();
                    default:
                        return false;
                }
            }
            else {
                return false;
            }
        },
        shouldTableBeDisabled(position) {
            // If both rules are viable, the table should be enabled
            if (this.isSkaterRuleViable() && this.isPositionRuleViable(position) ) {
                return false;
            }
            // If only one rule is viable, check if the rules are met
            else if (this.isSkaterRuleViable() || this.isPositionRuleViable(position) ) {
                if (this.isSkaterRuleViable()) {
                    return this.isSkaterRuleMet();
                }
                else {
                    return this.isPositionRuleMet(position);
                }
            }
            // Default to showing the table
            else {
                return false;
            }
        },
        shouldGoalieTableBeDisabled() {
            let numGoaliesProtected = this.getCurrTeamProtectedMap[this.getGoaliesString].length;
            return (numGoaliesProtected >= 1);
        },
        isSkaterRuleViable() {
            let numDefensemenProtected = this.getCurrTeamProtectedMap[this.getDefensemenString].length;
            let numForwardsProtected = this.getCurrTeamProtectedMap[this.getForwardsString].length;
            let numSkatersProtected = numDefensemenProtected + numForwardsProtected;
            return numSkatersProtected <= 8;
        },
        isPositionRuleViable() { 
            let numDefensemenProtected = this.getCurrTeamProtectedMap[this.getDefensemenString].length;
            let numForwardsProtected = this.getCurrTeamProtectedMap[this.getForwardsString].length;
            return numDefensemenProtected <= 3 && numForwardsProtected <= 7;
        },
        isSkaterRuleMet() {
            let numDefensemenProtected = this.getCurrTeamProtectedMap[this.getDefensemenString].length;
            let numForwardsProtected = this.getCurrTeamProtectedMap[this.getForwardsString].length;
            let numSkatersProtected = numDefensemenProtected + numForwardsProtected;
            return numSkatersProtected >= 8;
        },
        isPositionRuleMet(position) {
            let numProtectedForPosition = this.getCurrTeamProtectedMap[position].length;
            if (position === this.getDefensemenString) {
                return numProtectedForPosition >= 3;
            }
            if (position === this.getForwardsString) {
                return numProtectedForPosition >= 7;
            }
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
