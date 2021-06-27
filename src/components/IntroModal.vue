<template>
    <b-modal no-close-on-backdrop size="lg" ref="intro-modal" id="intro-modal">
        <b-container v-if="currentPage==0">
            <b-container class="py-4">
                <h1>Welcome to the NHL Expansion Draft Optimizer!</h1>
            </b-container>
            <b-container class="py-4">
                <p>In this tutorial, you will be running our optimizer on your favourite NHL team for the upcoming NHL Expansion Draft. We will be focusing on one team for the tutorial, but the optimizer lets you modify options, manually protect and/or expose players for every team in the league.</p>
                <p>Please see our <b-link :to="'faq'">FAQ</b-link > if you have any more questions.</p>
            </b-container>
        </b-container>
        <b-container v-if="currentPage==1">
            <b-container class="py-4">
                <h3>Which team do you want to act as?</h3>
            </b-container>
            <b-container class="py-4">
                <b-form-select v-model="chosenTeamIndex" :options="this.allTeams"></b-form-select>
            </b-container>
        </b-container>
        <b-container v-if="currentPage==2">
            <b-container class="py-4">
                <h3>Choose your performance metric</h3>
            </b-container>
            <b-container class="py-3">
                <p>This determines the metric the optimizer will use to rate your players.</p>
            </b-container>
            <b-container class="py-3">
                <b-form-select v-model="performanceMetric" :options="this.performanceMetrics"></b-form-select>
            </b-container>
            <b-container class="py-4">
                <h3>Choose your finanical flexibility metric</h3>
            </b-container>
            <b-container class="py-3">
                <p>This determines the metric the optimizer will use to determine financial flexibility for your team.</p>
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
        </b-container>
        <b-container v-if="currentPage==4">
            <b-row class="py-2">
                <b-col>
                    <h3>Summary</h3>
                </b-col>
            </b-row>
            <b-row class="py-2">
                <b-col>
                    <b-table-simple fixed outlined class="py-4 panel panel-default panel-table text-center">
                        <b-tbody>
                            <b-tr>
                                <b-th class="table-header">Team Name</b-th>
                                <b-td>{{ getChosenTeamName }}</b-td>
                            </b-tr>
                            <b-tr>
                                <b-th class="table-header">Performance Metric</b-th>
                                <b-td>{{ getCurrPerformanceMetricText }}</b-td>
                            </b-tr>
                            <b-tr>
                                <b-th class="table-header">Finanical Metric</b-th>
                                <b-td>{{ getCurrFinancialMetricText }}</b-td>
                            </b-tr>
                            <b-tr>
                                <b-th class="table-header">Preferred Metric</b-th>
                                <b-td>{{ getPreferredMetricText }}</b-td>
                            </b-tr>
                        </b-tbody>
                    </b-table-simple>
                </b-col>
            </b-row>
            <b-row class="py-2">
                <b-col>
                    <p>If you are happy with your options, press Optimize and wait for your results.</p>
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
            // todo: make this more data driven?
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
            'getCurrPerformanceMetricText'
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
                console.log(response);
                if (response && response.data && response.data.message) {
                    this.$bvModal.msgBoxOk(response.data.message);
                }
                }, error => {
                // TODO: show errors properly
                console.log(error);
            });
        },
        ...mapActions([
            'optimize'
        ])
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
