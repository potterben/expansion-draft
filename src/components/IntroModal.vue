<template>
    <div>
        <b-modal no-close-on-backdrop size="lg" ref="intro-modal" id="intro-modal">
            <b-container v-if="currentPage==0">
                <b-container class="py-4">
                    <h1>Welcome to the NHL Expansion Draft Optimizer!</h1>
                </b-container>
                <b-container class="py-4">
                    <p>This tool optimizes the protections made by existing teams and the selections made by the Seattle Kraken for the 2021 NHL Expansion Draft. The optimization is based on performance and finanical metrics that you will choose, and you can even weight which metric you think is more important. For existing teams, the tool protects players to minimize the value of exposed players based on your chosen metrics. For Seattle, the tool selects the players that maximizes your chosen metrics. Note that this is not a predictor, so protections and selections may vary as you change your metrics and weighting of those metrics.</p>
                    <p>In this tutorial, you will be running our optimizer on your favourite NHL team for the 2021 NHL Expansion Draft. We will be focusing on one team for the tutorial, but the optimizer lets you modify the same metrics, and you can also manually protect and/or expose players for every team in the league.</p>
                    <p>Please see our <b-link :to="'faq'" :target="'_blank'">FAQ</b-link > if you have any more questions.</p>
                </b-container>
            </b-container>
            <b-container v-if="currentPage==1">
                <b-container class="py-4">
                    <h3>Choose your favourite team and see how your choices affect your team</h3>
                </b-container>
                <b-container class="py-4">
                    <b-form-select v-model="chosenTeamIndex" :options="this.allTeams"></b-form-select>
                </b-container>
            </b-container>
            <b-container v-if="currentPage==2">
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
                    <h3>Choose the finanical flexibility metric the optimizer will use</h3>
                </b-container>
                <b-container class="py-3">
                    <b-form-select v-model="financialMetric" :options="this.financialMetrics"></b-form-select>
                </b-container>
            </b-container>
            <b-container v-if="currentPage==3">
                <b-container class="py-2">
                    <h3>Do you prefer player performance or financial flexibility?</h3>
                </b-container>
                <b-container>
                    <p>You can choose which metric is more important and the optimizer will use that preference when it makes its decisions.</p> 
                    <p>Consider your team's current state and what makes the most sense for your future. If your team is a contender, then you would likely value performance more. If your team is rebuilding, you would likely value financial flexibility.</p>
                </b-container>
                <b-container class="text-center">
                    <TeamSlider :teamName="getChosenTeamName" :isExpansionTeam="true" v-if="isExpansionTeamChosen" />
                    <TeamSlider :teamName="getChosenTeamName" :teamIndex="chosenTeamIndex" v-else/>
                </b-container>
                <b-row class="py-2">
                    <b-col>
                        <p>If you are happy with your options, press "Optimize" and wait for your results.</p>
                    </b-col>
                </b-row>
                <b-row class="py-2">
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
                        <p>If you are unsatisfied with the results, try manually modify some protections or change your chosen metrics in Advanced Options.</p>
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
            totalPages: 4,
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
                console.log(error);
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
