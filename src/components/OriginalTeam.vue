<template>
    <b-container>
        <TeamRequirementTable/>
        <b-button-group>
            <b-button @click="resetCurrTeamCheckboxes">Reset {{ teamName }}</b-button>
            <b-button @click="resetAllTeamCheckboxes">Reset all teams</b-button>
        </b-button-group>
        <SelectedPlayerTable :teamInit="teamInit"/>
        <PlayerTable position="forwards"/>
        <PlayerTable position="defensemen"/>
        <PlayerTable position="goalies"/>
   </b-container>
</template>

<script>
import TeamRequirementTable from './TeamRequirementTable.vue'
import PlayerTable from './PlayerTable.vue'
import SelectedPlayerTable from './SelectedPlayerTable.vue'
import { mapActions } from 'vuex'

export default {
    name: 'TeamTable',

    components: {
        TeamRequirementTable,
        PlayerTable,
        SelectedPlayerTable
    },

    props: {
        teamInit: String,
        teamName: String,
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
