import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        currTeam: null,
        teamSelection: [],
        parameters: [],
        results: []
      },
      mutations: {
        setCurrTeam(state, team){
            state.currTeam = team;
        }
      },
	actions: {
		setCurrTeam(context, team){
            context.commit("setCurrTeam", team);
        }
	},
	getters: {
        getCurrTeamAbbreviation(state)
        {
            return state.currTeam.abbreviation;
        },
        getCurrTeamName(state)
        {
            return state.currTeam.name;
        }
	}
})