<template>
    <b-container class='main-area' >
        <b-container class="text-center py-5">
            <h1>NHL Expansion Draft Optimizer</h1>
        </b-container>
        <b-card no-body>
            <b-tabs content-class="mt-3" align="center" pills card> 
                <b-tab title="Original Teams" active>
                    <b-container class="py-2 text-center">
                        <b-row class="col-12 py-1">
                            <b-col>
                                <h3>Select a team</h3>
                            </b-col>
                        </b-row>
                        <b-row class="col-12 py-1">
                            <b-col>
                                <b-form-select v-model="currentIndex" :options="this.originalTeamsOptions" class="text-center"/>
                            </b-col>
                        </b-row>
                    </b-container>
                    <b-container v-show="this.currentTeam" class="text-center py-4">
                        <TeamTable v-for="team in currentTeam" :key="team.abbreviation" :teamName="team.name" :teamInit="team.abbreviation" />
                    </b-container>
                </b-tab>
                <b-tab title="Optimizer Results">
                    <b-container v-show="this.expansionTeam" class="text-center py-4">
                        <TeamTable :teamName="expansionTeam.name" :teamInit="expansionTeam.abbreviation" :isExpansionTeam="true" />
                    </b-container>
                </b-tab>
            </b-tabs>
        </b-card>
    </b-container>
</template>

<script>
import TeamTable from './TeamTable.vue'
import TeamInfoJson from '../../store/data/TeamsInfo.json'
import { mapActions, mapGetters, mapState } from 'vuex'
// import { Swiper, SwiperSlide } from 'vue-awesome-swiper'

export default {
    name: 'MainArea',

    // Need to the originalTeams object in local scope so WebPack can get the static image files at compile time
    data() {
        return {
            originalTeams: TeamInfoJson.originalTeams,
            swiperOptions: {
                slidesPerView: 12,
                spaceBetween: 15,
                slideToClickedSlide: true,
                centeredSlides: true,
                loop: true,
                navigation: {
                    nextEl: '.swiper-button-next',
                    prevEl: '.swiper-button-prev'
                }
            }
        }
    },

    components: {
        TeamTable,
        // Swiper,
        // SwiperSlide
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
            'allTeams',
            "expansionTeam"
        ]),
        ...mapGetters([
            "getCurrTeamName"
        ])
    },

    methods: {
        ...mapActions([
            'setCurrTeamIndex'
        ]),
        handleDropdownClick(a) {
            console.log(a);
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

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
