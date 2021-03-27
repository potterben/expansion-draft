<template>
<footer>
	<b-container class = 'center'>
		<b-container>
			<b-button block variant="primary" id ='optimize'>Optimize</b-button>
		</b-container>
		<b-container class="text-center">
			<b-link v-b-modal.parameters id="parameters">Advanced Options</b-link>
		</b-container>
		<b-modal size="xl" id="parameters" hide-footer title="Optimizer Options">
			<b-container id="parameter-center">
				<b-row>
					<b-col>
					Financial Flexibility
					</b-col>
					<b-col>
					On-Ice Performance
					</b-col>
				</b-row>
				<b-row>
					<b-col>
						<!--  TODO: Make this data driven -->	
						<select class='combobox' id ='team-financial'>
							<option value='cap_hit_17_18' selected="selected">Cap Hit (17/18)</option>
							<option value='cap_hit_total'>Cap Hit '17 On</option>
						</select>
					</b-col>
					<b-col>
						<!--  TODO: Make this data driven -->
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
					</b-col>
				</b-row>
				<b-row>
					<b-col>
						<input type="checkbox" id ="ufa">
						<label for="ufa">Don't Consider UFAs</label>
					</b-col>
					<b-col/>
				</b-row>
				<TeamSlider />
				<TeamSlider :team_name="getCurrTeamName" />
				</b-container>
		</b-modal>
  </b-container>
  </footer>
</template>

<script>
import TeamSlider from './TeamSlider.vue'
import { mapGetters } from 'vuex'


export default {
  name: 'FooterArea',
  components: {
    TeamSlider
  },
  data () {
    return {
      value: 0
    }
  },
  computed: {
    ...mapGetters([
      'getCurrTeamName'
    ])
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
</style>
