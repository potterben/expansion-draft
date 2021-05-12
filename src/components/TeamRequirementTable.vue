<template>
    <b-container class="py-4 text-center">
        <b-row>
            <b-col sm="6">
                <b-row class ="py-2">
                    <b-col cols="12">
                        <h4>Protection Requirements</h4>
                    </b-col>
                </b-row>
                <b-row>
                    <b-col cols="12">
                        <b-table-simple outlined class=" mx-4 center-text panel panel-default panel-table">
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
                                    <template v-for="requirement in protectionRequirements">

                                        <b-td :key="requirement.position" :class="meetsProtectionRequirements(requirement) ? '' : 'fails-requirements'">
                                            {{ protectedCount(requirement.ids) }}/{{ requirement.limit }}
                                        </b-td>
                                    </template>
                                </b-tr>
                            </b-tbody>
                        </b-table-simple>
                    </b-col>
                </b-row>
            </b-col>
            <b-col sm="6">
                <b-row class ="py-2">
                    <b-col cols="12">
                        <h4>Exposure Requirements</h4>
                    </b-col>
                </b-row>
                <b-row >
                    <b-col cols="12">
                        <b-table-simple outlined class="mx-4 panel panel-default panel-table">
                            <b-thead>
                                <b-tr class="table-header">
                                    <b-td v-for="requirement in exposureRequirements" :key="requirement.position">
                                        {{ requirement.position }}
                                    </b-td>
                                </b-tr>
                            </b-thead>
                            <b-tbody>
                                <b-tr>
                                    <b-td v-for="requirement in exposureRequirements" :key="requirement.position" :class="meetsExposureRequirements(requirement) ? '' : 'fails-requirements'">
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
                    if (!this.isEmpty(this.getCurrTeamProtectedMap))
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
        },
        meetsProtectionRequirements(requirement) {
            let protectedCount = this.protectedCount(requirement.ids);
            let protectedLimit = requirement.limit;
            let meetsProtectionRequirements =  protectedLimit >= protectedCount;

            if (meetsProtectionRequirements) {
                this.removeFromCurrTeamDoesNotMeetProtectReqs(require.position);
            }
            else {
                this.addToCurrTeamDoesNotMeetProtectReqs(require.position);
            }

            return meetsProtectionRequirements;
        },
        meetsExposureRequirements(requirement) {
            let exposureCount = this.exposedCount(requirement.ids);
            let exposureLimit = requirement.limit;
            let meetsExposureRequirements = exposureCount >= exposureLimit;

            if (meetsExposureRequirements) {
                this.removeFromCurrTeamDoesNotMeetExposeReqs(require.position);
            }
            else {
                this.addToCurrTeamDoesNotMeetExposeReqs(require.position);
            }

            return meetsExposureRequirements;
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
