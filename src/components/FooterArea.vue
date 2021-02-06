<template>
  <footer id='collapse' class='navbar-inverse navbar-fixed-bottom'>
		<div class ='fluid-container'>
			<div class = 'parameter-heading'>
				<div class ="buttons" id ="wrapper">
					<button type='button' class='btn btn-default btn-lg' id = 'optimize'>Optimize</button>
				</div>
				<div class ="buttons" id ="wrapper">
					<a class='btn btn-default collapsed' data-toggle='collapse' href='#parameters'>Advanced Options</a>
				</div>
			</div>
			<div id='parameters' class = 'collapse'>
				<div class = 'fluid-container'>
					<div class = "row">
						<div class = "col-md-3">
							<div class ="row">
								<button type='button' class='btn btn-danger' id = "default">Reset checkboxes</button>
							</div>>
							<div class ="row">
								<label class="white">
									<input type="checkbox" id ="ufa">Don't Consider UFAs
								</label>
							</div>
						</div>
						<div class = "col-md-6">
							<div class=" parameter-center">
							<table id = "top-parameters">
								<tbody>
									<tr>
										<td></td>
										<td class = "white">Vegas Golden Knights</td>
										<td></td>
									</tr>
									<tr>
										<td class = "white">Financial Flexibility</td>
										<td class = "slider"><vue-slider v-model="value" /></td>
										<td class= "white">On-Ice Performance</td>
									</tr>
									<tr>
										<td>
											<select class='combobox' id ='team-financial'>
												<option value='cap_hit_17_18' selected="selected">Cap Hit (17/18)</option>
												<option value='cap_hit_total'>Cap Hit '17 On</option>
											</select>
										</td>
										<td class = "white">Settings for Other 30 Teams</td>
										<td>
											<select class='combobox' id ='team-value'>
												<option value='ps_16_17' selected="selected">Point Shares (16/17)</option>
												<option value='ps_15_16'>Point Shares (15/16)</option>
												<option value='ps_14_15'>Point Shares (14/15)</option>
												<option value='gaps_16_17'>Adjusted Point Shares (16/17)</option>
												<option value='ps_avg'>Average Point Shares</option>
												<option value='gvt_15_16'>GVT (15/16)</option>
												<option value='gvt_14_15'>GVT (14/15)</option>
												<option value='gvt_avg'>Average GVT</option>
												<option value='ea_rating'>EA Rating</option>
											</select>
										</td>
									</tr>
									<tr>
										<td></td>
										<td class = "slider"><input id='ex31' data-provide="slider" data-slider-tooltip="hide" data-slider-id='allTeams' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
										<td></td>
									</tr>
									<tr>
										<td></td>
										<td>
											<label class="white">
													<input type="checkbox" id="master">Apply to all 30 teams
											</label>
										</td>
										<td></td>
									</tr>
								</tbody>
							</table>
							</div>
						</div>
						<div class = "col-md-3">
						</div>
					</div>
					<div class ="row">
						<div class ="col-md-4">
							<table class = "sliders">
								<tbody>
									<tr>
										<td><p class = "white">Anaheim Ducks</p></td>
										<td class = "slider"><input  id='ex1' data-slider-tooltip="hide" data-slider-id='ANA' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">Arizona Coyotes</p></td>
										<td class = "slider"><input data-provide="slider" id='ex2' data-slider-tooltip="hide" data-slider-id='ARI' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">Boston Bruins</p></td>
										<td class = "slider"><input id='ex3' data-slider-tooltip="hide" data-slider-id='BOS' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">Buffalo Sabres</p></td>
										<td class = "slider"><input id='ex4' data-slider-tooltip="hide" data-slider-id='BUF' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">Calgary Flames</p></td>
										<td class = "slider"><input id='ex5' data-slider-tooltip="hide" data-slider-id='CGY' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">Carolina Hurricanes</p></td>
										<td class = "slider"><input id='ex6' data-slider-tooltip="hide" data-slider-id='CAR' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">Chicago Blackhawks</p></td>
										<td class = "slider"><input id='ex7' data-slider-tooltip="hide" data-slider-id='CHI' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">Colorado Avalanche</p></td>
										<td class = "slider"><input id='ex8' data-slider-tooltip="hide" data-slider-id='COL' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">Columbus Blue Jackets</p></td>
										<td class = "slider"><input id='ex9' data-slider-tooltip="hide" data-slider-id='CBJ' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">Dallas Stars</p></td>
										<td class = "slider"><input id='ex10' data-slider-tooltip="hide" data-slider-id='DAL' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
								</tbody>
							</table>
						</div>
						<div class ="col-md-4">
							<table class = "sliders">
								<tbody>
									<tr>
										<td><p class = "white">Detroit Red Wings</p></td>
										<td class = "slider"><input id='ex11' data-slider-tooltip="hide" data-slider-id='DET' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">Edmonton Oilers</p></td>
										<td class = "slider"><input id='ex12' data-slider-tooltip="hide" data-slider-id='EDM' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">Florida Panthers</p></td>
										<td class = "slider"><input id='ex13' data-slider-tooltip="hide" data-slider-id='FLA' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">Los Angeles Kings</p></td>
										<td class = "slider"><input id='ex14' data-slider-tooltip="hide" data-slider-id='LAK' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">Minnesota Wild</p></td>
										<td class = "slider"><input id='ex15' data-slider-tooltip="hide" data-slider-id='MIN' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">Montreal Canadiens</p></td>
										<td class = "slider"><input id='ex16' data-slider-tooltip="hide" data-slider-id='MTL' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">Nashville Predators</p></td>
										<td class = "slider"><input id='ex17' data-slider-tooltip="hide" data-slider-id='NSH' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">New Jersey Devils</p></td>
										<td class = "slider"><input id='ex18' data-slider-tooltip="hide" data-slider-id='NJD' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">New York Islanders</p></td>
										<td class = "slider"><input id='ex19' data-slider-tooltip="hide" data-slider-id='NYI' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">New York Rangers</p></td>
										<td class = "slider"><input id='ex20' data-slider-tooltip="hide" data-slider-id='NYR' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
								</tbody>
							</table>
						</div>
						<div class ="col-md-4 ">
							<table class = "sliders">
								<tbody>
									<tr>
										<td><p class = "white">Ottawa Senators</p></td>
										<td class = "slider"><input id='ex21' data-slider-tooltip="hide" data-slider-id='OTT' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">Philadelphia Flyers</p></td>
										<td class = "slider"><input id='ex22' data-slider-tooltip="hide" data-slider-id='PHI' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">Pittsburgh Penguins</p></td>
										<td class = "slider"><input id='ex23' data-slider-tooltip="hide" data-slider-id='PIT' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">San Jose Sharks</p></td>
										<td class = "slider"><input id='ex24' data-slider-tooltip="hide" data-slider-id='SJS' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">St. Louis Blues</p></td>
										<td class = "slider"><input id='ex25' data-slider-tooltip="hide" data-slider-id='STL' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">Tampa Bay Lightning</p></td>
										<td class = "slider"><input id='ex26' data-slider-tooltip="hide" data-slider-id='TBL' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">Toronto Maple Leafs</p></td>
										<td class = "slider"><input id='ex27' data-slider-tooltip="hide" data-slider-id='TOR' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">Vancouver Canucks</p></td>
										<td class = "slider"><input id='ex28' data-slider-tooltip="hide" data-slider-id='VAN' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">Washington Capitals</p></td>
										<td class = "slider"><input id='ex29' data-slider-tooltip="hide" data-slider-id='WAS' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
									<tr>
										<td><p class = "white">Winnipeg Jets</p></td>
										<td class = "slider"><input id='ex30' data-slider-tooltip="hide" data-slider-id='WPJ' type='text' data-slider-min='0' data-slider-max='1' data-slider-step='0.1' data-slider-value='1'/></td>
									</tr>
								</tbody>
							</table>
						</div>
					</div>
				</div>
			</div>
		</div>
	</footer>
</template>

<script>
import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/antd.css'

export default {
  name: 'FooterArea',
  components: {
    VueSlider
  },
  data () {
    return {
      value: 0
    }
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
