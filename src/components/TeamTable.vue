<template>
    <div class = 'team-table' :id ="teamInit">
            <template v-if="!isExpansionTeam">
                <TeamRequirementTable/>
                <b-button-group>
                    <b-button @click="resetCurrTeamCheckboxes">Reset {{ teamName }}</b-button>
                    <b-button @click="resetAllTeamCheckboxes">Reset all teams</b-button>
                </b-button-group>
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
import { mapActions } from 'vuex'

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
    },

    methods: {
        ...mapActions([
            "resetCurrTeamCheckboxes",
            "resetAllTeamCheckboxes"
        ])
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
