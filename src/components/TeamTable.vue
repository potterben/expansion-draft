<template>
    <div class = 'team-table' :id ="teamInit">
        <h2 v-bind:class="teamInit">
            {{ teamName }}
        </h2>
        <div class = "fluid-container top-center">
            <table class="panel panel-default panel-table">
                <thead>
                    <tr>
                        <td colspan="3">Protection Requirements</td>
                        <td colspan="3">Exposure Requirements</td>
                    </tr>
                </thead>
                <tbody id = "requirements">
                    <tr>
                        <td>F</td>
                        <td>D</td>
                        <td>G</td>
                        <td>F</td>
                        <td>D</td>
                        <td>G</td>
                    </tr>
                    <tr>
                        <td>-/7</td>
                        <td>-/3</td>
                        <td>-/1</td>
                        <td>-/2</td>
                        <td>-/1</td>
                        <td>-/1</td>
                    </tr>
                    <tr>
                            <td colspan="2">-/8</td>
                            <td>-/1</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class='table-responsive scrollable'>
            <PlayerTable positionId="forward" positionTitle="Forwards" />
            <PlayerTable positionId="defence" positionTitle="Defensemen" />
            <PlayerTable positionId="goalie" positionTitle="Goalies" />
        </div>
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
