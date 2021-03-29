<template>
    <div class='fluid-container theme-showcase' role='main'>
        <div class = 'fluid-container center'>
            <img v-for="(team, index) in this.originalTeams" :key="team.abbreviation" :src="require('../assets/nhl_logos/' + team.imageLocation)" :id="team.abbreviation" :index="index" @click="handleImgClick($event)"/>
        </div>
        <div class = 'row'>
            <div class = 'col-md-6 black' id= "left" v-if="this.currentTeam">
                <TeamTable v-for="team in currentTeam" :key="team.abbreviation" :teamName="team.name" :teamInit="team.abbreviation" />
            </div>
            <div class = 'col-md-6 black' id = "right">
                <TeamTable v-if="expansionTeam" :teamName="expansionTeam.name" :teamInit="expansionTeam.abbreviation" />
            </div>
        </div>
    </div>
</template>

<script>
import TeamTable from './TeamTable.vue'
import TeamInfoJson from '../../store/data/TeamsInfo.json'
import { mapState, mapActions } from 'vuex'

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
            return this.originalTeams.filter(team => team.abbreviation === this.currTeamAbbreviation);
        },
        ...mapState({
            currTeamAbbreviation: state => state.currTeam.abbreviation,
            expansionTeam: state => state.expansionTeam
        })
    },

    methods: {
        ...mapActions([
            'setCurrTeam'
        ]),
        handleImgClick: function (event)
        {
            var index = event.target.attributes.index.value;
            this.setCurrTeam(index);
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
