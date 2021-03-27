<template>
    <div class = 'team-table' :id ="teamInit">
        <h2 v-bind:class="teamInit">
            {{ teamName }}
        </h2>
        <!-- make this data driven -->
        <b-container class = "top-center">
            <b-table-simple class="panel panel-default panel-table">
                <b-thead>
                    <b-tr>
                        <b-td colspan="3">Protection Requirements</b-td>
                        <b-td colspan="3">Exposure Requirements</b-td>
                    </b-tr>
                </b-thead>
                <b-tbody id = "requirements">
                    <b-tr>
                        <b-td>F</b-td>
                        <b-td>D</b-td>
                        <b-td>G</b-td>
                        <b-td>F</b-td>
                        <b-td>D</b-td>
                        <b-td>G</b-td>
                    </b-tr>
                    <b-tr>
                        <b-td>-/7</b-td>
                        <b-td>-/3</b-td>
                        <b-td>-/1</b-td>
                        <b-td>-/2</b-td>
                        <b-td>-/1</b-td>
                        <b-td>-/1</b-td>
                    </b-tr>
                    <b-tr>
                        <b-td colspan="2">-/8</b-td>
                        <b-td colspan="4">1</b-td>
                    </b-tr>
                </b-tbody>
            </b-table-simple>
        </b-container>
        <b-container class='table-responsive scrollable'>
            <PlayerTable positionId="forward" positionTitle="Forwards" />
            <PlayerTable positionId="defence" positionTitle="Defensemen" />
            <PlayerTable positionId="goalie" positionTitle="Goalies" />
        </b-container>
    </div>
</template>

<script>
import PlayerTable from './PlayerTable.vue'

export default {
    name: 'TeamTable',

    components: {
        PlayerTable
    },

    props: {
        teamInit: String,
        teamName: String
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
