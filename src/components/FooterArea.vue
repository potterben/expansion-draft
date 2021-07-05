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
                        <b-form-checkbox id ="ufa" v-model="dontConsiderUFAState">
                            Try to avoid UFAs <b-icon icon="question-circle" v-b-tooltip.hover title="Checking this option means the optimizer will try to avoid protecting/selecting UFAs as they are not under contract for the upcoming season." />
                        </b-form-checkbox>
                    </b-col>
                    <b-col class="col-6"/>
                </b-row>
                <b-img :src="require('../assets/nhl_logos/' + expansionTeam.imageLocation)" :alt="expansionTeam.name" :title="expansionTeam.name" class="small-seattle-logo"/>
                <TeamSlider :teamName="expansionTeam.name" :isExpansionTeam="true" v-if="expansionTeam" />
                <TeamSlider :teamName="'All Existing Teams'" v-show="applyToAll"/>
                <b-collapse id="all-other-teams" v-model="doNotApplyToAll">
                    <template v-for="team in allOtherTeams">
                        <b-img :src="require('../assets/nhl_logos/' + team.imageLocation)" :key="'img'+team.abbreviation" :alt="team.name" :title="team.name" class="small-team-logo"/>
                        <TeamSlider :key="team.name" :teamName="team.name" :teamIndex="team.index"/>
                    </template>
                </b-collapse>
            </b-container>
            <template #modal-footer>
                <b-row class="col-12">
                    <b-col cols=6 align-h="center">
                        <b-link class="toggle" v-b-toggle="'all-other-teams'">
                            <template v-if="doNotApplyToAll">
                                <b-icon icon="chevron-up" aria-hidden="true"></b-icon>
                                Hide all existing teams
                            </template>
                            <template v-else>
                                <b-icon icon="chevron-down" aria-hidden="true"></b-icon>
                                Show all existing teams
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
        dontConsiderUFAState: {
            get() {
                return this.dontConsiderUFAs;
            },
            set(value) {
                this.setDontConsiderUFAs(value);
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
            'dontConsiderUFAs',
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
            .then(response => {response},
             error => {
                let options = {"okVariant":"info", "noCloseOnBackdrop": true, "hideHeader": false, "hideHeaderClose": false};
                this.$bvModal.msgBoxOk(error.response.data.detail, options);
            });
        },
        ...mapActions([
            'optimize',
            'setCurrFinancialMetric',
            'setCurrPerformanceMetric',
            'setDontConsiderUFAs',
            'setApplyToAllOriginalTeams',
        ])
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
