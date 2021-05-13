<template>
    <b-container class='main-area' >
        <b-container class="text-center py-5">
            <h1>NHL Expansion Draft Optimizer</h1>
        </b-container>
        <b-card no-body>
            <b-tabs content-class="mt-3" align="center" pills card> 
                <b-tab title="Original Teams" active>
                    <b-container class="py-4">
                        <b-row class="col-12 py-1 justify-content-center">
                            <h2>Team Selector</h2>
                        </b-row>
                        <b-row class="col-12 py-1 justify-content-center">
                            <h5>Click to choose a team</h5>
                        </b-row>
                        <b-row class="col-12 py-4">
                            <swiper ref="teamSelectionSwiper" :options="swiperOptions" @slideChange="handleSwiperIndexChanged">
                                <template v-for="(team, index) in this.originalTeams">
                                    <swiper-slide :key="index">
                                        <img :src="require('../assets/nhl_logos/' + team.imageLocation)" :id="team.abbreviation"/>
                                    </swiper-slide>
                                </template>
                                <div class="swiper-button-prev" slot="button-prev"></div>
                                <div class="swiper-button-next" slot="button-next"></div>
                            </swiper>
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
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'

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
        Swiper,
        SwiperSlide
    },

    computed: {
        swiper () {
            return this.$refs.teamSelectionSwiper.$swiper;
            },
        currentTeam: function () {
            if (this.originalTeams) {
                return [this.originalTeams[this.currTeamIndex]];
            }
            return [];
        },
        ...mapState([
            "currTeamIndex",
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
