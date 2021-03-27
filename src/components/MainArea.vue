<template>
    <div class='fluid-container theme-showcase' role='main'>
        <div class = 'fluid-container center'>
            <img v-for="team in teamData.originalTeams" :key="team.abbreviation" :src="require('../assets/nhl_logos/' + team.imageLocation)" :id="team.abbreviation" v-on:click="setCurrTeam(team)"/>
        </div>
        <div class = 'row'>
            <div class = 'col-md-6 black' id= "left">
                <TeamTable v-for="team in currentTeam" :key="team.abbreviation" :teamName="team.name" :teamInit="team.abbreviation" />
            </div>
            <div class = 'col-md-6 black' id = "right">
                <TeamTable teamName="Vegas Golden Knights" teamInit="VGK" />
            </div>
        </div>
    </div>
</template>

<script>
import TeamTable from './TeamTable.vue'
import { mapGetters, mapActions } from 'vuex'

export default {
    name: 'MainArea',

    components: {
        TeamTable
    },

    inject : [
        'teamData',
        'metrics'
    ],

    computed: {
        currentTeam: function () {
            return this.teamData.originalTeams.filter(team => team.abbreviation === this.getCurrTeamAbbreviation);
        },
        ...mapGetters([
        'getCurrTeamAbbreviation'
        ])
    },

    created() {
        this.setCurrTeam(this.teamData.originalTeams[0]);
    },

    methods: {
        ...mapActions([
            'setCurrTeam',
            'setCurrFinancialMetric',
            'setCurrPerformanceMetric'
        ])
    },
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
