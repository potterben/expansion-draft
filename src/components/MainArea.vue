<template>
	<div class='fluid-container theme-showcase' role='main'>
		<div class = 'fluid-container center'>
            ICONS GO HERE
		</div>
		<div class = 'row'>
			<div class = 'col-md-6 black' id= "left">
                <TeamTable team_name="Anaheim Ducks" team_init="ANA" />
            </div>
			<div class = 'col-md-6 black' id = "right">
                <TeamTable team_name="Vegas Golden Knights" team_init="VGK" />
			</div>
		</div>
	</div>
</template>

<script>
import TeamTable from './TeamTable.vue'

export default {
  name: 'MainArea',
    components: {
    TeamTable
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
