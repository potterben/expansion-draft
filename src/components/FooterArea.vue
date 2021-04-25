<template>
    <footer class="footer py-4 fixed-bottom">
        <b-row class="col-12 py-1" align-h="center">
            <b-button variant="info" id='optimize'>Optimize</b-button>
        </b-row>
        <b-row class="col-12 text-center py-1" align-h="center">
            <b-link v-b-modal.advanced-options id="advanced-options">Advanced Options</b-link>
        </b-row>
        <b-modal scrollable size="xl" id="advanced-options" title="Advanced Options">
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
                <TeamSlider :teamName="getCurrTeamName" v-if="getCurrTeamName"/>
                <TeamSlider v-for="team in allOtherTeams" :key="team.name" :teamName="team.name" :teamIndex="team.index"/>

            </b-container>
            <template #modal-footer>
                <b-form-checkbox id="applyToAll" v-model="applyToAll">
                    Sync all original teams sliders
                </b-form-checkbox>
                <b-button variant="info" block :pressed.sync="showAllOtherTeams">
                    {{ showAllOtherTeams ? "Hide all other teams":"Show all other teams" }}
                </b-button>
            </template>
        </b-modal>
    </footer>
</template>

<script>
import TeamSlider from './TeamSlider.vue'
import { mapState, mapActions, mapGetters } from 'vuex'

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
                return this.originalTeams.filter(team => team.index !== this.currTeamIndex);
            }
            return [];
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
            'applyToAllOriginalTeams',
            'showAllOtherOriginalTeams'
        ]),
        ...mapGetters([
            'getCurrTeamName'
        ])

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
</style>
