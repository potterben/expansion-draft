<template>
    <footer class="footer py-4 fixed-bottom">
        <b-row class="col-12 py-1" align-h="center">
            <b-button variant="info" id='optimize' @click="runOptimizer">Optimize Results</b-button>
        </b-row>
        <b-row class="col-12 text-center py-1" align-h="center">
            <b-link v-b-modal.advanced-options id="advanced-options">Advanced Options</b-link>
        </b-row>
        <b-modal scrollable size="lg" id="advanced-options" title="Advanced Options" @hide="onAdvancedOptionsHidden">
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
                        <b-form-select v-model="financialMetric" :options="this.financialMetrics" @change="onMetricChanged"></b-form-select>
                    </b-col>
                    <b-col class="col-6 py-2">
                        <b-form-select v-model="performanceMetric" :options="this.performanceMetrics" @change="onMetricChanged"></b-form-select>
                    </b-col>
                </b-row>
                <b-row>
                    <b-col class="col-12 py-2">
                        <b-form-checkbox id ="ufa" v-model="dontConsiderUFAState">
                            <p> Try to avoid UFAs <b-link class="custom-tooltip" v-b-tooltip.hover title="Checking this option means the optimizer will try to avoid protecting/selecting UFAs as they are not under contract for the upcoming season.">
                            <b-icon icon="question-circle" aria-label="Help"/></b-link></p>
                        </b-form-checkbox>
                    </b-col>
                </b-row>
                <b-row>
                    <b-col class="col-12 py-2">
                        <b-form-checkbox id ="age" v-model="adjustForAgeState">
                             <p>Adjust for player age <b-link class="custom-tooltip" v-b-tooltip.hover title="Checking this option means the optimizer will try to protect/select younger players over older players.">
                            <b-icon icon="question-circle" aria-label="Help"/></b-link></p>
                        </b-form-checkbox>
                    </b-col>
                </b-row>
                <b-img :src="require('../assets/nhl_logos/' + expansionTeam.imageLocation)" :alt="expansionTeam.name" :title="expansionTeam.name" class="pt-4 small-seattle-logo"/>
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
                <b-container>
                    <b-link class="toggle float-left" v-b-toggle="'all-other-teams'">
                            <template v-if="doNotApplyToAll">
                                <b-icon icon="chevron-up" aria-hidden="true"></b-icon>
                                Hide all existing teams
                            </template>
                            <template v-else>
                                <b-icon icon="chevron-down" aria-hidden="true"></b-icon>
                                Show all existing teams
                            </template>
                        </b-link>
                        <b-button class="float-right" variant="info" id='optimize' @click="onOptimizeInAdvancedSettings">Optimize</b-button>
                </b-container>
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
    
    data: function() {
        return {
            optionChanged: false
        }
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
        adjustForAgeState: {
            get() {
                return this.adjustForAge;
            },
            set(value) {
                this.setAdjustForAge(value);
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
            'adjustForAge',
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
        onMetricChanged() {
            this.optionChanged = true;
        },
        hideModals() {
            this.$bvModal.hide("intro-modal");
            this.$bvModal.hide("advanced-options");
        },
        runOptimizer() { 
            this.hideModals();
            asyncLoading(this.optimize())
            .then(response => {response},
             error => {
                let options = {"okVariant":"info", "noCloseOnBackdrop": true, "hideHeader": false, "hideHeaderClose": false};
                this.$bvModal.msgBoxOk(error.response.data.detail, options);
            });
        },
        onAdvancedOptionsHidden() {
            if (this.optionChanged) {
                this.showResetModal();
            }
        },
        showResetModal(run_optimizer) {
            this.$bvModal.msgBoxConfirm('You have changed your options. Do you have want to reset all your checkboxes?', {
                buttonSize: 'sm',
                okVariant: 'info',
                title: 'Reset checkboxes',
                okTitle: 'Reset',
                cancelTitle: 'Do Not Reset',
                footerClass: 'p-2',
                noCloseOnBackdrop: true,
                centered: true
            }).then(value => {
                if (value) {
                    this.resetAllTeamCheckboxes();
                }
            }).catch({
            }).finally(() =>{
                if (run_optimizer) {
                    this.runOptimizer();
                }
            })
            this.optionChanged = false;

        },
        onOptimizeInAdvancedSettings() {
            if (this.optionChanged) {
                this.showResetModal(true);
            }
            else {
                this.runOptimizer();
            }
        },
        ...mapActions([
            'optimize',
            'setCurrFinancialMetric',
            'setCurrPerformanceMetric',
            'setDontConsiderUFAs',
            'setApplyToAllOriginalTeams',
            'resetAllTeamCheckboxes',
            'setAdjustForAge'
        ])
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
