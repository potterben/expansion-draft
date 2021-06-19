<template>
    <b-container class="py-4 text-center">
        <b-row>
            <b-col lg="6">
                <b-row class ="py-2">
                    <b-col cols="12">
                        <h4>Protection Requirements</h4>
                    </b-col>
                </b-row>
                <b-row>
                    <b-col cols="12">
                        <b-table-simple fixed outlined class="panel panel-default panel-table">
                            <b-thead>
                                <b-tr class="table-header">
                                    <b-td v-for="requirement in protectionRequirements" :key="requirement.position" >
                                        {{ requirement.position }}
                                    </b-td>
                                </b-tr>
                            </b-thead>
                            <b-tbody id = "requirements">
                                <b-tr class="table-row">

                                </b-tr>
                                <b-tr class="table-row">
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
                        <h4>Exposure Requirements</h4>
                    </b-col>
                </b-row>
                <b-row >
                    <b-col cols="12">
                        <b-table-simple fixed outlined class="panel panel-default panel-table">
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

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
