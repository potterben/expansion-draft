<template>
	<div class='fluid-container theme-showcase' role='main'>
		<div class = 'fluid-container center'>
      <img :src="require('../assets/nhl_logos/Anaheim.png')" id = 'ANA'/>
      <img :src="require('../assets/nhl_logos/Arizona.png')" id = 'ARI'/>
      <img :src="require('../assets/nhl_logos/Boston.png')" id = 'BOS'/>
      <img :src="require('../assets/nhl_logos/Buffalo.png')" id = 'BUF'/>
      <img :src="require('../assets/nhl_logos/Calgary.png')" id = 'CGY'/>
      <img :src="require('../assets/nhl_logos/Carolina.png')" id = 'CAR'/>
      <img :src="require('../assets/nhl_logos/Chicago.png')" id = 'CHI'/>
      <img :src="require('../assets/nhl_logos/Colorado.png')" id = 'COL'/>
      <img :src="require('../assets/nhl_logos/Columbus.png')" id = 'CBJ'/>
      <img :src="require('../assets/nhl_logos/Dallas.png')" id = 'DAL'/>
      <img :src="require('../assets/nhl_logos/Detroit.png')" id = 'DET'/>
      <img :src="require('../assets/nhl_logos/Edmonton.png')" id = 'EDM'/>
      <img :src="require('../assets/nhl_logos/Florida.png')" id = 'FLA'/>
      <img :src="require('../assets/nhl_logos/Los Angeles.png')" id = 'LAK'/>
      <img :src="require('../assets/nhl_logos/Minnesota.png')" id = 'MIN'/>
      <img :src="require('../assets/nhl_logos/Montreal.png')" id = 'MTL'/>
      <img :src="require('../assets/nhl_logos/Nashville.png')" id = 'NSH'/>
      <img :src="require('../assets/nhl_logos/New Jersey.png')" id = 'NJD'/>
      <img :src="require('../assets/nhl_logos/New York 1.png')" id = 'NYI'/>
      <img :src="require('../assets/nhl_logos/New York 2.png')" id = 'NYR'/>
      <img :src="require('../assets/nhl_logos/Ottawa.png')" id = 'OTT'/>
      <img :src="require('../assets/nhl_logos/Philadelphia.png')" id = 'PHI'/>
      <img :src="require('../assets/nhl_logos/Pittsburgh.png')" id = 'PIT'/>
      <img :src="require('../assets/nhl_logos/San Jose.png')" id = 'SJS'/>
      <img :src="require('../assets/nhl_logos/St. Louis.png')" id = 'STL'/>
      <img :src="require('../assets/nhl_logos/Tampa Bay.png')" id = 'TBL'/>
      <img :src="require('../assets/nhl_logos/Toronto.png')" id = 'TOR'/>
      <img :src="require('../assets/nhl_logos/Vancouver.png')" id = 'VAN'/>
      <img :src="require('../assets/nhl_logos/Washington.png')" id = 'WAS'/>
      <img :src="require('../assets/nhl_logos/Winnipeg.png')" id = 'WPJ'/>
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
