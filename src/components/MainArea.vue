<template>
    <b-container class='theme-showcase' role='main'>
        <b-card no-body>
            <b-tabs content-class="mt-3" align="center" pills card>
                <b-tab title="Original Teams" active>
                    <b-container v-if="this.currentTeam" class="centered-text">
                        <span class="inline">
                            <h5>Team Selector:</h5>
                            <p> Click to choose a team</p>
                        </span>
                        <b-row class="center" align-h="center">
                            <img v-for="(team, index) in this.originalTeams" :key="team.abbreviation" :src="require('../assets/nhl_logos/' + team.imageLocation)" :id="team.abbreviation" :index="index" @click="handleImgClick($event)"/>
                        </b-row>
                        <TeamTable v-for="team in currentTeam" :key="team.abbreviation" :teamName="team.name" :teamInit="team.abbreviation" />
                    </b-container>
                </b-tab>
                <b-tab title="Results">
                    <b-container v-if="this.expansionTeam" class="centered-text">
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
a {
  color: #42b983;
}
</style>
