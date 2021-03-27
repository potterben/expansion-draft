import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        currTeam: null,
        currFinancialMetric: null,
        currPerformanceMetric: null,
        teamSelection: [],
        parameters: [],
        results: []
      },
      mutations: {
        setCurrTeam(state, team) {
            state.currTeam = team;
        },
        setCurrFinancialMetric(state, financialMetric) {
            state.currFinancialMetric = financialMetric;
        },
        setCurrPerformanceMetric(state, performanceMetric) {
            state.currPerformanceMetric = performanceMetric;
        }
      },
    actions: {
        setCurrTeam(context, team) {
            context.commit("setCurrTeam", team);
        },
        setCurrFinancialMetric(context, financialMetric) {
            context.commit("setCurrFinancialMetric", financialMetric);
        },
        setCurrPerformanceMetric(context, performanceMetric) {
            context.commit("setCurrPerformanceMetric", performanceMetric);
        }
    },
    getters: {
        getCurrTeamAbbreviation(state) {
            return state.currTeam.abbreviation;
        },
        getCurrTeamName(state) {
            return state.currTeam.name;
        }
	}
})