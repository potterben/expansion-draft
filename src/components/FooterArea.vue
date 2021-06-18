<template>
    <footer class="footer py-4 fixed-bottom">
        <b-row class="col-12 py-1" align-h="center">
            <b-button variant="info" id='optimize' @click="showOptimizeDialog">Optimize Results</b-button>
        </b-row>
        <b-row class="col-12 text-center py-1" align-h="center">
            <b-link v-b-modal.advanced-options id="advanced-options">Advanced Options</b-link>
        </b-row>
        <b-modal scrollable size="lg" id="advanced-options" title="Advanced Options">
            <b-container class="text-center py-4">
                <b-row>
                    <b-col class="col-6 py-2">
                    Financial Flexibility
                    </b-col>
                    <b-col class="col-6 py-2">
                    On-Ice Performance
                    </b-col>
                </b-row>
                <b-row>
                    <b-col class="col-6 py-2">
                        <b-form-select v-model="financialMetric" :options="this.financialMetrics"></b-form-select>
                    </b-col>
                    <b-col class="col-6 py-2">
                        <b-form-select v-model="performanceMetric" :options="this.performanceMetrics"></b-form-select>
                    </b-col>
                </b-row>
                <b-row>
                    <b-col class="col-6 py-2">
                        <b-form-checkbox id ="ufa" v-model="considerUFAState">
                            Don't Consider UFAs
                        </b-form-checkbox>
                    </b-col>
                    <b-col class="col-6"/>
                </b-row>
                <TeamSlider :teamName="expansionTeam.name" :isExpansionTeam="true" v-if="expansionTeam" />
                <TeamSlider :teamName="'All Original Teams'" v-show="applyToAll"/>
                <b-collapse id="all-other-teams" v-model="doNotApplyToAll">
                    <TeamSlider v-for="team in allOtherTeams" :key="team.name" :teamName="team.name" :teamIndex="team.index"/>
                </b-collapse>
            </b-container>
            <template #modal-footer>
                <b-row class="col-12">
                    <b-col cols=6 align-h="center">
                        <b-link class="toggle" v-b-toggle="'all-other-teams'">
                            <template v-if="doNotApplyToAll">
                                <b-icon icon="chevron-up" aria-hidden="true"></b-icon>
                                Hide all other teams
                            </template>
                            <template v-else>
                                <b-icon icon="chevron-down" aria-hidden="true"></b-icon>
                                Show all other teams
                            </template>
                        </b-link>
                    </b-col>
                </b-row>
            </template>
        </b-modal>
    </footer>
</template>

<script>
import TeamSlider from './TeamSlider.vue'
import { mapState, mapActions, mapGetters } from 'vuex'
import { asyncLoading } from 'vuejs-loading-plugin'

export default {
    name: 'FooterArea',

    components: {
        TeamSlider
    },

    computed: {
        financialMetric: {
            get() {
                return this.currFinancialMetric;
            },
            set(value) {
                this.setCurrFinancialMetric(value);
            }
        },
        performanceMetric: {
            get() {
                return this.currPerformanceMetric;
            },
            set(value) {
                this.setCurrPerformanceMetric(value);
            }
        },
        considerUFAState: {
            get() {
                return this.considerUFAs;
            },
            set(value) {
                this.setConsiderUFAs(value);
            }
        },
        applyToAll: {
            get() {
                return this.applyToAllOriginalTeams;
            },
            set(value) {
                this.setApplyToAllOriginalTeams(value);
            }
        },
        doNotApplyToAll: {
            get() {
                return !this.applyToAllOriginalTeams;
            },
            set(value) {
                this.setApplyToAllOriginalTeams(!value);
            }
        },
        allOtherTeams() {
            return this.originalTeams;
        },
        ...mapState([
            'currFinancialMetric',
            'financialMetrics',
            'currPerformanceMetric',
            'performanceMetrics',
            'expansionTeam',
            'originalTeams',
            'currTeamIndex',
            'considerUFAs',
            'applyToAllOriginalTeams'
        ]),
        ...mapGetters([
            'getCurrTeamName'
        ])
    },

    methods: {
        showOptimizeDialog() { 
            // TODO: make this function shared with intromodal
            // Hide all modals
            this.$bvModal.hide("intro-modal");
            this.$bvModal.hide("advanced-options");
            
            asyncLoading(this.optimize())
            .then(response => {
                if (response && response.data && response.data.message) {
                    this.$bvModal.msgBoxOk(response.data.message);
                }
                }, error => {
                // TODO: show errors properly
                console.log(error);
            });
        },
        ...mapActions([
            'optimize',
            'setCurrFinancialMetric',
            'setCurrPerformanceMetric',
            'setConsiderUFAs',
            'setApplyToAllOriginalTeams',
        ])
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
