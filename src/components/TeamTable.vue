<template>
    <div class = 'team-table' :id ="teamInit">
        <b-row class="py-4 col-12 justify-content-center"> 
            <h2 v-bind:class="teamInit">
                {{ teamName }}
            </h2>
        </b-row>
            <template v-if="!isExpansionTeam">
                <TeamRequirementTable/>
                <PlayerTable position="forwards"/>
                <PlayerTable position="defensemen"/>
                <PlayerTable position="goalies"/>
            </template>
            <template v-else>
                <ExpansionPlayerTable position="forwards"/>
                <ExpansionPlayerTable position="defensemen"/>
                <ExpansionPlayerTable position="goalies"/>
            </template>

   </div>
</template>

<script>
import TeamRequirementTable from './TeamRequirementTable.vue'
import PlayerTable from './PlayerTable.vue'
import ExpansionPlayerTable from './ExpansionPlayerTable.vue'

export default {
    name: 'TeamTable',

    components: {
        TeamRequirementTable,
        PlayerTable,
        ExpansionPlayerTable
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
</style>
