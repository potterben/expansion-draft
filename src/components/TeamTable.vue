<template>
    <div class = 'team-table' :id ="teamInit">
        <h2 v-bind:class="teamInit">
            {{ teamName }}
        </h2>
        <b-container class = "top-center">
            <TeamRequirementTable v-if="!isExpansionTeam"/>
        </b-container>
        <b-container >
            <PlayerTable positionId="f" positionTitle="Forwards" />
            <PlayerTable positionId="d" positionTitle="Defensemen" />
            <PlayerTable positionId="g" positionTitle="Goalies" />
        </b-container>
    </div>
</template>

<script>
import TeamRequirementTable from './TeamRequirementTable.vue'
import PlayerTable from './PlayerTable.vue'

export default {
    name: 'TeamTable',

    components: {
        TeamRequirementTable,
        PlayerTable
    },

    props: {
        teamInit: String,
        teamName: String,
        isExpansionTeam: {
            type: Boolean,
            default: false
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h2 {
  text-align: center;
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
