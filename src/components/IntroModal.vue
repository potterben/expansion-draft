<template>
    <div>
        <b-modal v-if="this.originalTeams && this.expansionTeam" scrollable no-close-on-backdrop size="lg" ref="intro-modal" id="intro-modal">
            <b-container v-if="currentPage==0">
                <b-container class="py-4">
                    <h1>NHL Expansion Draft Optimizer</h1>
                </b-container>
                <b-container class="py-2">
                    <b-row class="py-2">
                        <b-col class="text-center">
                            <b-img :src="require('../assets/expansion_draft_logo.png')" :alt="'NHL Expansion Draft Logo'" :title="'NHL Expansion Draft Logo'" class="expansion-draft-logo"/>
                        </b-col>
                    </b-row>
                    <b-row class="py-2">
                        <b-col>
                            <h3>What is happening?</h3>
                        </b-col>
                    </b-row>
                    <b-row class="py-2">
                        <b-col>
                            <p>Seattle is joining the NHL as the newest expansion team for the 2021-2022 season. As part of the expansion, they get to draft one player from each team. Each team can protect a certain number of players to prevent them from being drafted by Seattle.</p>
                        </b-col>
                    </b-row>
                    <b-row class="py-2">
                        <b-col>
                            <h3>What is this site?</h3>
                        </b-col>
                    </b-row>
                    <b-row >
                        <b-col>
                            <p>It allows fans to play ‘Armchair GM’ and simulate the optimal drafting and protection decisions made by Seattle and the other teams.</p>
                        </b-col>
                    </b-row>
                </b-container>
            </b-container>
            <b-container v-if="currentPage==1">
                <b-container class="py-4">
                    <h1>NHL Expansion Draft Optimizer</h1>
                </b-container>
                <b-container class="py-2">
                    <b-row class="py-2">
                        <b-col>
                            <h3>How does this site work?</h3>
                        </b-col>
                    </b-row>
                    <b-row class="py-2">
                        <b-col>
                            <p>You can choose objectives for current teams and Seattle in terms of whether they should try to get the best on-ice performance or financial flexibility. We then run an optimizer to maximize each team's objectives.</p>
                        </b-col>
                    </b-row>
                    <b-row class="py-2">
                        <b-col>
                            <h3>How do I use this site?</h3>
                        </b-col>
                    </b-row>
                    <b-row class="py-2">
                        <b-col>
                            <p>To start, we will walk you through an optimization of the draft.</p>
                            <p>First choose your team to optimize. Then choose from a number of player performance and financial flexibility metrics. You can even weigh the importance of each metric based on what you think your team should optimize. Our optimizer will then simulate what each team should do to maximize these objectives.</p>
                            <p>Afterwards, you can modify the simulated decisions by changing team objectives or manually protecting and exposing players. Try re-simulating the outcomes under different objectives to get the best outcomes.</p>
                        </b-col>
                    </b-row>
                </b-container>
            </b-container>
            <b-container class="text-center" v-if="currentPage==2">
                <b-row class="py-4">
                    <b-col>
                        <h3>Choose your favourite team and see how your choices affect your team</h3>
                    </b-col>
                </b-row>
                <b-row class="py-4">
                    <b-col cols=12>
                        <b-form-select v-model="chosenTeamIndex" :options="this.allTeams"></b-form-select>
                    </b-col>
                </b-row>
                <b-row class="py-4">
                    <b-col cols=12 >
                        <template v-for="team in chosenTeam">
                            <b-img :src="require('../assets/nhl_logos/' + team.imageLocation)" :key="'img'+team.abbreviation" :alt="team.name" :title="team.name" class="team-logo"/>
                        </template>
                    </b-col>
                </b-row>

            </b-container>
            <b-container v-if="currentPage==3">
                <b-container class="py-4">
                    <h3>Choose the performance metric the optimizer will use</h3>
                </b-container>
                <b-container class="py-3">
                    <b-form-select v-model="performanceMetric" :options="this.performanceMetrics"></b-form-select>
                </b-container>
                <b-container class="py-3">
                    <p>{{ getCurrPerformanceMetricDescription }} </p>
                </b-container>
                <b-container class="py-4">
                    <h3>Choose the financial flexibility metric the optimizer will use</h3>
                </b-container>
                <b-container class="py-3">
                    <b-form-select v-model="financialMetric" :options="this.financialMetrics"></b-form-select>
                </b-container>
            </b-container>
            <b-container v-if="currentPage==4">
                <b-container class="py-1">
                    <h3>Do you prefer player performance or financial flexibility?</h3>
                </b-container>
                <b-container>
                    <p>You can choose which metric is more important and the optimizer will use that preference when it makes its decisions.</p> 
                    <p>Consider your team's current state and what makes the most sense for your future. If your team is a contender, then you would likely value performance more. If your team is rebuilding, you would likely value financial flexibility.</p>
                </b-container>
                <b-container class="text-center">
                    <template v-for="team in chosenTeam">
                        <b-img :src="require('../assets/nhl_logos/' + team.imageLocation)" :key="'img'+team.abbreviation" :alt="team.name" :title="team.name" class="small-team-logo"/>
                        <TeamSlider :key="team.name" :teamName="team.name" :teamIndex="team.index" :isExpansionTeam="isExpansionTeamChosen()"/>
                    </template>
                </b-container>
                <b-row>
                    <b-col>
                        <p>If you are happy with your options, press "Optimize" and wait for your results.</p>
                    </b-col>
                </b-row>
                <b-row>
                    <b-col>
                        <b-form-checkbox v-model="doNotShowIntroModal" value="checked" unchecked-value="unchecked">
                            Do not show this tutorial for any future visits.
                        </b-form-checkbox>
                    </b-col>
                </b-row>
            </b-container>
            <template #modal-footer>
                <b-container>
                    <b-button type="button" class="btn btn-info"  @click="previousPage" v-if="!firstPage">
                        Back
                    </b-button>
                    <b-button type="button" class="btn btn-info float-right" v-if="!lastPage" @click="nextPage" :disabled="lastPage" >
                        Next
                    </b-button>
                    <b-button type="submit" class="btn btn-info float-right" v-if="lastPage" @click="showOptimizeDialog">
                        Optimize
                    </b-button>
                </b-container>
            </template>
        </b-modal>
        <b-modal no-close-on-backdrop size="lg" ref="results-modal" id="results-modal" :ok-variant="'info'" :ok-only="true">
            <b-container>
                <b-row class="py-4">
                    <b-col cols=12>
                        <h3>Here are your optimization results!</h3>
                    </b-col>
                </b-row>
                <b-row>
                    <b-col cols=12>
                        <p>These results based on your choice of performance and finanical metrics, and your weighing of each metric.</p>
                        <p>If you are unsatisfied with the results, try changing your chosen metrics in Advanced Options.</p>
                    </b-col>
                </b-row>
                <b-row class="text-center">
                    <b-col cols=12>
                        <b-img :src="require('../assets/screenshots/advanced_options.png')"/>
                    </b-col>
                </b-row>
                <b-row class="pt-4">
                    <b-col cols=12>
                        <p>You can also try manually modifying some protections and/or selections to fine tune your results.</p>
                    </b-col>
                </b-row>
                <b-row class="py-2 text-center">
                    <b-col cols=12>
                        <b-img :src="require('../assets/screenshots/protect_expose.png')"/>
                    </b-col>
                </b-row>
                <b-row class="py-2 text-center">
                    <b-col cols=12>
                        <b-img :src="require('../assets/screenshots/keep_remove.png')"/>
                    </b-col>
                </b-row>
            </b-container>
        </b-modal>
    </div>
</template>

<script>
import TeamSlider from './TeamSlider.vue'
import { mapState, mapActions, mapGetters } from 'vuex'
import { asyncLoading } from 'vuejs-loading-plugin'

export default {
    name: 'IntroModal',

    data() {
        return {
            doNotShowIntroModal: "unchecked",
            currentPage: 0,
            totalPages: 5,
            chosenTeamIndex: 0
        }
    },

    mounted() {
        // Check if we need to show the modal
        if (localStorage.doNotShowIntroModal) {
            this.doNotShowIntroModal = localStorage.doNotShowIntroModal;
        }
        if (this.doNotShowIntroModal == "unchecked") {
            this.showModal();
        }
        // Initialize as the Kraken
        this.chosenTeamIndex = this.allTeams.length -1;
    },

    watch: {
        doNotShowIntroModal(value) {
            localStorage.doNotShowIntroModal = value;
        }
    },

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
        getChosenTeamName: function() {
            return this.allTeams.find(team => team.value === this.chosenTeamIndex).text;
        },
        chosenTeam: function () {
            if (!this.isExpansionTeamChosen() && this.originalTeams) {
                return [this.originalTeams[this.chosenTeamIndex]];
            }
            if (this.isExpansionTeamChosen() && this.expansionTeam) {
                return [this.expansionTeam];
            }
            return [];
        },
        getPreferredMetricText() {
            let percentage = 0;
            if (this.chosenTeamIndex == (this.allTeams.length -1)) {
                percentage = this.expansionTeam.alpha;
            }
            else {
                percentage= this.originalTeams[this.chosenTeamIndex].beta;
            }
            if (percentage >= 50) {
                return this.getCurrFinancialMetricText;
            }
            else {
                return this.getCurrPerformanceMetricText;
            }
        },
        firstPage() {
            return this.currentPage === 0;
        },
        lastPage() {
            return this.currentPage === (this.totalPages - 1);
        },
        ...mapState([
            'currFinancialMetric',
            'financialMetrics',
            'currPerformanceMetric',
            'performanceMetrics',
            'allTeams',
            'originalTeams',
            'expansionTeam'
        ]),
        ...mapGetters([
            'getCurrFinancialMetricText',
            'getCurrFinancialMetricDescription',
            'getCurrPerformanceMetricText',
            'getCurrPerformanceMetricDescription'
        ])
    },

    methods: {
        showModal() {
            this.$refs['intro-modal'].show()
        },
        isExpansionTeamChosen() {
            return this.chosenTeamIndex === (this.allTeams.length -1);
        },
        nextPage() {
            this.currentPage++;
        },
        previousPage() {
            this.currentPage--;
        },
        showOptimizeDialog() {
            // Hide all modals
            this.$bvModal.hide("intro-modal");
            this.$bvModal.hide("advanced-options");
            
            asyncLoading(this.optimize())
            .then(response => {
                if (response && response.data) {
                    this.$bvModal.show("results-modal");
                }
            }, error => {
                let options = {"okVariant":"info", "noCloseOnBackdrop": true, "hideHeader": false, "hideHeaderClose": false};
                this.$bvModal.msgBoxOk(error.response.data.detail, options);
            });
        },
        ...mapActions([
            'optimize',
            'setCurrPerformanceMetric',
            'setCurrFinancialMetric'
        ])
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
