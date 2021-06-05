<template>
    <div class = 'team-table' :id ="teamInit">
        <b-row class="py-4 col-12 justify-content-center"> 
            <h2 v-bind:class="teamInit">
                {{ teamName }}
            </h2>
        </b-row>
            <TeamRequirementTable v-show="!isExpansionTeam"/>
            <PlayerTable position="forwards" />
            <PlayerTable position="defensemen" />
            <PlayerTable position="goalies" />
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
</style>
