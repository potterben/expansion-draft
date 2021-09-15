<template>
    <b-container class="py-4 text-center">
        <b-row>
            <b-col lg="6">
                <b-row class ="py-2">
                    <b-col cols="12">
                        <h4>Protection Requirements <b-link class="custom-tooltip" v-b-tooltip.hover title="Each team can protect either 7 forwards and 3 defensemen and 1 goalie, or 8 skaters (forwards and defensemen) and 1 goalie. If you manually protect players and meet these requirements, the tables will be greyed out so you cannot protect additional players.">
                                  <b-icon icon="question-circle" aria-label="Help"/></b-link>
                        </h4> 
                    </b-col>
                </b-row>
                <b-row>
                    <b-col cols="12">
                        <b-table-simple outlined class="panel panel-default panel-table">
                            <b-thead>
                                <b-tr class="table-header">
                                    <b-td v-for="requirement in protectionRequirements" :key="requirement.position" >
                                        {{ requirement.position }}
                                    </b-td>
                                </b-tr>
                            </b-thead>
                            <b-tbody>
                                <b-tr>
                                    <b-td v-for="requirement in protectionRequirements" :key="requirement.position">
                                        {{ protectedCount(requirement.ids) }}/{{ requirement.limit }}
                                    </b-td>
                                </b-tr>
                            </b-tbody>
                        </b-table-simple>
                    </b-col>
                </b-row>
            </b-col>
            <b-col lg="6">
                <b-row class ="py-2">
                    <b-col cols="12">
                        <h4>Exposure Requirements <b-link class="custom-tooltip" v-b-tooltip.hover title="Each team must expose a minimum number of players for each postions. For more information, please see the FAQ.">
                        <b-icon icon="question-circle" aria-label="Help"/></b-link>
                        </h4>
                    </b-col>
                </b-row>
                <b-row >
                    <b-col cols="12">
                        <b-table-simple outlined class="panel panel-default panel-table">
                            <b-thead>
                                <b-tr class="table-header">
                                    <b-td v-for="requirement in exposureRequirements" :key="requirement.position">
                                        {{ requirement.position }}
                                    </b-td>
                                </b-tr>
                            </b-thead>
                            <b-tbody>
                                <b-tr>
                                    <b-td v-for="requirement in exposureRequirements" :key="requirement.position">
                                        {{ exposedCount(requirement.ids) }}/{{ requirement.limit }}
                                    </b-td>
                                </b-tr>
                            </b-tbody>
                        </b-table-simple>
                    </b-col>
                </b-row>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
import ConstraintsInfoJson from "../../store/data/ConstraintsInfo.json"
import { mapGetters, mapActions } from 'vuex'

export default {
    name: 'TeamRequirementTable',

    data() {
        return {
            protectionRequirements: ConstraintsInfoJson.protectionRequirements,
            exposureRequirements: ConstraintsInfoJson.exposureRequirements
        }
    },

    computed: {
        ...mapGetters([
            'getCurrTeamProtectedMap',
            'getCurrTeamMeetsRequirementsMap'
        ]),
        protectedCount() {
            return ids => {
                var count = 0;
                ids.forEach(id => {
                    if (this.getCurrTeamProtectedMap !== null)
                    {
                        count += this.getCurrTeamProtectedMap[id].length;
                    }
                });
                return count
            }
        },
        exposedCount() {
            return ids => {
                var count = 0;
                ids.forEach(id => {
                    if (!this.isEmpty(this.getCurrTeamMeetsRequirementsMap))
                    {
                        count += this.getCurrTeamMeetsRequirementsMap[id];
                    }
                });
                return count
            }
        }
    },

    methods: {
        ...mapActions([
            'addToCurrTeamDoesNotMeetProtectReqs',
            'removeFromCurrTeamDoesNotMeetProtectReqs',
            'addToCurrTeamDoesNotMeetExposeReqs',
            'removeFromCurrTeamDoesNotMeetExposeReqs'
        ]),
        isEmpty(object) {
            return object && Object.keys(object).length === 0 && object.constructor === Object;
        }
    }
}
</script>
