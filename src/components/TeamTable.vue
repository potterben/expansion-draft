<template>
    <div class = 'team-table' v-bind:id ="team_init">
        <h2 v-bind:class="team_init">{{ team_name }}</h2>
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
            <PlayerTable position_id="forward" position_title="Forwards" />
            <PlayerTable position_id="defence" position_title="Defensemen" />
            <PlayerTable position_id="goalie" position_title="Goalies" />
        </div>
    </div>
</template>

<script>
import PlayerTable from './PlayerTable.vue'

export default {
  name: 'TeamTable',
  props: {
    team_init: String,
    team_name: String
  },
  components: {
      PlayerTable
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
