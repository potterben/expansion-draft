<template>
    <footer id="footer">
        <b-container class = 'center'>
            <b-container>
                <b-button block variant="primary" id ='optimize'>Optimize</b-button>
            </b-container>
            <b-container class="text-center">
                <b-link v-b-modal.parameters id="parameters">Advanced Options</b-link>
            </b-container>
            <b-modal scrollable size="xl" id="parameters" title="Optimizer Options">
                <b-container id="parameter-center">
                    <b-row>
                        <b-col>
                        Financial Flexibility
                        </b-col>
                        <b-col>
                        On-Ice Performance
                        </b-col>
                    </b-row>
                    <b-row>
                        <b-col>
                            <b-form-select v-model="financialMetric" :options="this.financialMetrics"></b-form-select>
                        </b-col>
                        <b-col>
                            <b-form-select v-model="performanceMetric" :options="this.performanceMetrics"></b-form-select>
                        </b-col>
                    </b-row>
                    <b-row>
                        <b-col>
                            <b-form-checkbox id ="ufa" v-model="considerUFAState">
                                Don't Consider UFAs
                            </b-form-checkbox>
                        </b-col>
                        <b-col/>
                    </b-row>
                    <TeamSlider :teamName="expansionTeam.name" :isExpansionTeam="true" v-if="expansionTeam" />
                    <TeamSlider :teamName="currTeam.name" v-if="currTeam"/>
                    <TeamSlider v-for="team in allOtherTeams" :key="team.name" :teamName="team.name"/>

                </b-container>
                <template #modal-footer>
                    <b-form-checkbox id = "applyToAll" v-model="applyToAll">
                        Sync all original teams sliders
                    </b-form-checkbox>
                    <b-button variant="info" block :pressed.sync="showAllOtherTeams">
                        {{ showAllOtherTeams ? "Hide all other teams":"Show all other teams" }}
                    </b-button>
                </template>
            </b-modal>
        </b-container>
    </footer>
</template>

<script>
import TeamSlider from './TeamSlider.vue'
import { mapState, mapActions } from 'vuex'

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
        showAllOtherTeams: {
            get() {
                return this.showAllOtherOriginalTeams;
            },
            set(value) {
                this.setShowAllOtherOriginalTeams(value);
            }
        },
        allOtherTeams: function () {
            if (this.showAllOtherTeams) {
                return this.originalTeams.filter(team => team.abbreviation !== this.currTeamAbbreviation);
            }
            return [];
        },
        ...mapState([
            'currFinancialMetric',
            'financialMetrics',
            'currPerformanceMetric',
            'performanceMetrics',
            'expansionTeam',
            'currTeam',
            'originalTeams',
            'considerUFAs',
            'applyToAllOriginalTeams',
            'showAllOtherOriginalTeams'
        ]),
        ...mapState ({
            currTeamAbbreviation: state => state.currTeam.abbreviation
        })
    },

    methods: {
        ...mapActions([
            'setCurrFinancialMetric',
            'setCurrPerformanceMetric',
            'setConsiderUFAs',
            'setApplyToAllOriginalTeams',
            'setShowAllOtherOriginalTeams'
        ])
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
    margin: 40px 0 0;
}
ul {
    list-style-type: none;
    padding: 0;
}
li {
    display: inline-block;
    margin: 0 10px;
}
</style>
