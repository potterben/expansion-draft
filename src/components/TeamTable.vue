<template>
    <div class = 'team-table' :id ="teamInit">
        <b-container class="text-center py-4">
            <h2 v-bind:class="teamInit">
                {{ teamName }}
            </h2>
        </b-container>
            <TeamRequirementTable v-if="!isExpansionTeam"/>
            <PlayerTable positionId="f" positionTitle="Forwards" />
            <PlayerTable positionId="d" positionTitle="Defensemen" />
            <PlayerTable positionId="g" positionTitle="Goalies" />
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
