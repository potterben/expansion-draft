<template>
    <b-container class='main-area' >
        <b-container class="text-center py-5">
            <h1>NHL Expansion Draft Optimizer</h1>
        </b-container>
        <b-card no-body>
            <b-tabs v-model="tabIndex" content-class="mt-3" align="center" pills card> 
                <b-tab title="Existing Teams">
                    <b-container class="py-2 text-center">
                        <b-row class="py-1">
                            <b-col cols=12>
                                <h3>Select a team</h3>
                            </b-col>
                        </b-row>
                        <b-row class="py-1">
                            <b-col cols=12>
                                <b-form-select v-model="currentIndex" :options="this.originalTeamsOptions" class="team-selector text-center"/>
                            </b-col>
                        </b-row>
                    </b-container>
                    <b-container v-show="this.currentTeam" class="text-center py-4">
                        <template v-for="team in currentTeam">
                            <b-img :src="require('../assets/nhl_logos/' + team.imageLocation)" :key="'img'+team.abbreviation" :alt="team.name" :title="team.name" class="team-logo"/>
                            <OriginalTeam :key="team.abbreviation" :teamName="team.name" :teamInit="team.abbreviation"/>
                        </template>
                    </b-container>
                </b-tab>
                <b-tab title="Seattle Kraken">
                    <b-container v-show="this.expansionTeam && this.expansionTeam.selected" class="text-center py-4">
                        <ExpansionTeam/>
                    </b-container>
                    <b-container v-show="this.expansionTeam && !this.expansionTeam.selected" class="text-center py-4">
                        <h3>Run the optimizer to get results</h3>
                    </b-container>
                </b-tab>
            </b-tabs>
        </b-card>
    </b-container>
</template>

<script>
import OriginalTeam from './OriginalTeam.vue'
import ExpansionTeam from './ExpansionTeam.vue'
import { mapActions, mapGetters, mapState } from 'vuex'

export default {
    name: 'MainArea',

    components: {
        OriginalTeam,
        ExpansionTeam
    },

    computed: {
        currentIndex: {
            get() {
                return this.currTeamIndex;
            },
            set(value) {
                this.setCurrTeamIndex(value);
            }
        },
        tabIndex: {
            get() {
                return this.currTabIndex;
            },
            set(value) {
                this.setCurrTabIndex(value);
            }
        },
        swiper () {
            return this.$refs.teamSelectionSwiper.$swiper;
        },
        currentTeam: function () {
            if (this.originalTeams) {
                return [this.originalTeams[this.currTeamIndex]];
            }
            return [];
        },
        originalTeamsOptions: function () {
            if (this.allTeams) {
                let originalTeamsOptions = this.allTeams.slice();
                originalTeamsOptions.shift();
                return originalTeamsOptions
            }
            return [];
        },
        ...mapState([
            "currTeamIndex",
            "currTabIndex",
            "allTeams",
            "expansionTeam",
            "originalTeams",
            "figureData",
            "currFinancialMetric",
            "currPerformanceMetric"
        ]),
        ...mapGetters([
            "getCurrTeamName",
            "getCurrFinancialMetricText",
            "getCurrPerformanceMetricText"
            
        ])
    },

    methods: {
        ...mapActions([
            'setCurrTeamIndex',
            'setCurrTabIndex'
        ]),
        handleDropdownClick() {
            var index = this.swiper.realIndex
            this.setCurrTeamIndex(index);
        },
        handleSwiperIndexChanged: function() {
            var index = this.swiper.realIndex
            this.setCurrTeamIndex(index);
        }
    }
}
</script>
