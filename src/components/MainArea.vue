<template>
    <b-container class='main-area' >
        <b-container class="text-center py-5">
            <h1>NHL Expansion Draft Optimizer</h1>
        </b-container>
        <b-card no-body fill>
            <b-tabs class="myTab" content-class="mt-3" align="center" pills card fill> 
                <b-tab title="Original Teams" active>
                    <b-container class="py-4">
                        <b-row class="col-12 py-1">
                            <h5>Team Selector:</h5>
                        </b-row>
                        <b-row class="col-12 py-1">
                            <p> Click to choose a team</p>
                        </b-row>
                        <b-row class="col-12 py-4">
                            <img v-for="(team, index) in this.originalTeams" :key="team.abbreviation" :src="require('../assets/nhl_logos/' + team.imageLocation)" :id="team.abbreviation" :index="index" @click="handleImgClick($event)"/>
                        </b-row>
                    </b-container>
                    <b-container v-if="this.currentTeam" class="text-center py-4">
                        <TeamTable v-for="team in currentTeam" :key="team.abbreviation" :teamName="team.name" :teamInit="team.abbreviation" />
                    </b-container>
                </b-tab>
                <b-tab title="Results">
                    <b-container v-if="this.expansionTeam" class="text-center py-4">
                        <TeamTable v-if="expansionTeam" :teamName="expansionTeam.name" :teamInit="expansionTeam.abbreviation" :isExpansionTeam="true" />
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

export default {
    name: 'MainArea',

    // Need to the originalTeams object in local scope so WebPack can get the static image files at compile time
    data() {
        return {
            originalTeams: TeamInfoJson.originalTeams
        }
    },

    components: {
        TeamTable
    },

    computed: {
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
        handleImgClick: function (event)
        {
            var index = event.target.attributes.index.value;
            this.setCurrTeamIndex(index);
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
