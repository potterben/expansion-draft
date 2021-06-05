<template>
    <b-modal no-close-on-backdrop size="lg" ref="intro-modal" id="intro-modal">
        <b-container v-if="currentPage==0">
            <b-container class="py-4">
                <h2>Welcome to the NHL Expansion Draft Optimizer!</h2>
            </b-container>
            <b-container class="py-4">
                <p>This tutorial will guide you through the optimizer. In this scenario, you will be optimizing for your favourite NHL team, but the tool allows you to tweak parameters for the whole league.</p>
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
            <b-container class="py-2">
                <h3>Choose your performance metric</h3>
            </b-container>
            <b-container class="py-2">
                <p>This determines the metric the optimizer will use to rate your players.</p>
            </b-container>
            <b-container class="py-4">
                <b-form-select v-model="performanceMetric" :options="this.performanceMetrics"></b-form-select>
            </b-container>
            <b-container class="py-2z">
                <h3>Choose your finanical flexibility metric</h3>
            </b-container>
            <b-container class="py-2">
                <p>This determines the metric the optimizer will use to determine financial flexibility for your team;</p>
            </b-container>
            <b-container class="py-4">
                <b-form-select v-model="financialMetric" :options="this.financialMetrics"></b-form-select>
            </b-container>
        </b-container>
        <b-container v-if="currentPage==3">
            <b-container class="py-2">
                <h3>How much do you value performance versus financial flexibility?</h3>
            </b-container>
            <b-container>
                <p>This determines which metric the optimizer will determine as more important. 
                    If your team is contending and you want to keep your best players, then you would likely value performance more.
                    If your team is rebuilding, you would likely want more financial flexibility, so you should value that higher</p>
            </b-container>
            <b-container class="text-center">
                <TeamSlider :teamName="getChosenTeamName" :isExpansionTeam="true" v-if="isExpansionTeamChosen" />
                <TeamSlider :teamName="getChosenTeamName" :teamIndex="chosenTeamIndex" v-else/>
            </b-container>
        </b-container>
        <b-container v-if="currentPage==4">
            <h3>Click Optimize and wait for your results!</h3>
            <b-container class="py-3">
                <b-form-checkbox
                v-model="doNotShowIntroModal"
                value="checked"
                unchecked-value="unchecked"
                >
                    Do not show this dialog for any future visits.
                </b-form-checkbox>
            </b-container>
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
import { mapState, mapActions } from 'vuex'
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
