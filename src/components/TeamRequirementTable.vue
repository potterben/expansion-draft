<template>
    <b-container class="py-4">
        <b-row>
            <b-col>
                <b-table-simple class="center-text panel panel-default panel-table">
                    <b-thead>
                        <b-tr class="table-header">
                            <b-td :colspan="protectionRequirements.length">Protection Requirements</b-td>
                        </b-tr>
                    </b-thead>
                    <b-tbody id = "requirements">
                        <b-tr class="table-row">
                            <b-td v-for="requirement in protectionRequirements" :key="requirement.position">
                                {{ requirement.position }}
                            </b-td>
                        </b-tr>
                        <b-tr class="table-row">
                            <b-td v-for="requirement in protectionRequirements" :key="requirement.position">
                                {{ protectedCount(requirement.ids) }}/{{ requirement.limit }}
                            </b-td>
                        </b-tr>
                    </b-tbody>
                </b-table-simple>
            </b-col>
            <b-col>
                <b-table-simple class=" panel panel-default panel-table">
                    <b-thead>
                        <b-tr class="table-header">
                            <b-td :colspan="exposureRequirements.length">Exposure Requirements</b-td>
                        </b-tr>
                    </b-thead>
                    <b-tbody id = "requirements">
                        <b-tr class="table-row">
                            <b-td v-for="requirement in exposureRequirements" :key="requirement.position">
                                {{ requirement.position }}
                            </b-td>
                        </b-tr>
                        <b-tr class="table-row">
                            <b-td v-for="requirement in exposureRequirements" :key="requirement.position">
                                {{ exposedCount(requirement.ids) }}/{{ requirement.limit }}
                            </b-td>
                        </b-tr>
                    </b-tbody>
                </b-table-simple>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
import ConstraintsInfoJson from "../../store/data/ConstraintsInfo.json"
import { mapGetters } from 'vuex'

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
        isEmpty(object) {
            return object && Object.keys(object).length === 0 && object.constructor === Object;
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
