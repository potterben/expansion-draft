import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import TeamInfoJson from './data/TeamsInfo.json'
import MetricsInfoJson from './data/MetricsInfo.json'

Vue.use(Vuex)

// TODO: separate into separate files
class Team {
    constructor(name, abbreviation) {
      this.name = name;
      this.abbreviation = abbreviation;
    }
  }
 
class OriginalTeam extends Team {
    constructor(name, abbreviation, index) {
        super(name, abbreviation);
        this.index = index;
        this.protected = {};
        this.exposed = {};
        this.beta = 0.0;
        this.constraints = {'f_p': 0, 'f_e': 0, 'd_p': 0, 'd_e': 0, 'g_p': 0, 'g_e': 0}
    }    
}

class ExpansionTeam extends Team {
    constructor(name, abbreviation) {
        super(name, abbreviation);
        this.keep = [];
        this.remove = [];
        this.alpha = 0.0;
    }    
}

const removeFromArray = (array, value) => {
    const newArray = [...array];
    const index = newArray.indexOf(value);
    if (index > -1) {
        newArray.splice(index, 1);
        return newArray;
    }
    else {
        return array;
    }
}

export default new Vuex.Store({
    state: {
        currTeamIndex: 0,
        originalTeams: [],

        expansionTeam: null,

        currFinancialMetric: "",
        financialMetrics: [],

        currPerformanceMetric: "",
        performanceMetrics: [],

        considerUFAs: false,
        applyToAllOriginalTeams: true,
        playerData: null
      },
      mutations: {
        setCurrTeamIndex(state, index) {
            state.currTeamIndex = index;
        },
        setOriginalTeams(state, originalTeams) {
            state.originalTeams = originalTeams;
        },
        setExpansionTeam(state, expansionTeam) {
            state.expansionTeam = expansionTeam;
        },
        setCurrFinancialMetric(state, financialMetric) {
            state.currFinancialMetric = financialMetric;
        },
        setFinancialMetrics(state, financialMetrics) {
            state.financialMetrics = financialMetrics;
        },
        setCurrPerformanceMetric(state, performanceMetric) {
            state.currPerformanceMetric = performanceMetric;
        },
        setPerformanceMetrics(state, performanceMetrics) {
            state.performanceMetrics = performanceMetrics;
        },
        setConsiderUFAs(state, considerUFAs) {
            state.considerUFAs = considerUFAs;
        },
        setCurrTeamSliderValue(state, value) {
            state.originalTeams[state.currTeamIndex].beta = value;
        },
        setOriginalTeamSliderValue(state, payload) {
            state.originalTeams[payload.index].beta = payload.value;
        },
        setAllOriginalTeamsSliderValue(state, value) {
            for (let i = 0; i < state.originalTeams.length; ++i) {
                state.originalTeams[i].beta = value;
            }
        },
        setExpansionTeamSliderValue(state, value) {
            state.expansionTeam.alpha = value;
        },
        setApplyToAllOriginalTeams(state, value) {
            state.applyToAllOriginalTeams = value;
        },
        setPlayerData(state, playerData) {
            state.playerData = playerData;
        },
        setOriginalTeamProtectedMap(state, payload) {
            state.originalTeams[payload.index].protected = payload.protectedMap;
        },
        addToCurrTeamProtectedMap(state, payload) {
            state.originalTeams[state.currTeamIndex].protected[payload.positionId].push(payload.id);
        },
        removeFromCurrTeamProtectedMap(state, payload) {
            const updatedArray = removeFromArray(state.originalTeams[state.currTeamIndex].protected[payload.positionId], payload.id);
            state.originalTeams[state.currTeamIndex].protected[payload.positionId] = updatedArray;
        },
        setOriginalTeamExposedMap(state, payload) {
            state.originalTeams[payload.index].exposed = payload.exposedMap;
        },
        addToCurrTeamExposedMap(state, payload) {
            state.originalTeams[state.currTeamIndex].exposed[payload.positionId].push(payload.id);
        },
        removeFromCurrTeamExposedMap(state, payload) {
            const updatedArray = removeFromArray(state.originalTeams[state.currTeamIndex].exposed[payload.positionId], payload.id);
            state.originalTeams[state.currTeamIndex].exposed[payload.positionId] = updatedArray;
        }
      },
    actions: {
        initializeTeamData(context) {
            let expansionTeam = TeamInfoJson.expansionTeam;
            let expansionTeamObject = new ExpansionTeam(expansionTeam[0].name, expansionTeam[0].abbreviation);
            context.commit("setExpansionTeam", expansionTeamObject);

            let originalTeams = TeamInfoJson.originalTeams;
            let originalTeamsArray = []
            for (let i =0; i < originalTeams.length; i++) {
                let teamToAdd = new OriginalTeam(originalTeams[i].name,originalTeams[i].abbreviation, i);
                originalTeamsArray.push(teamToAdd);
            }
            context.commit("setOriginalTeams", originalTeamsArray);
        },
        initializeLoadMetrics(context) {
            let financialMetrics = MetricsInfoJson.financialMetrics;
            let financialMetricsArray = [];
            for (let i =0; i < financialMetrics.length; i++)
            {
                if (i === 0) {
                    context.commit("setCurrFinancialMetric", financialMetrics[i].value);
                }
                financialMetricsArray.push(financialMetrics[i]);
            }
            context.commit("setFinancialMetrics", financialMetricsArray);
            
            let performanceMetrics = MetricsInfoJson.performanceMetrics
            let performanceMetricsArray = []
            for (let i=0; i < performanceMetrics.length; i++)
            {
                if (i === 0) {
                    context.commit("setCurrPerformanceMetric", performanceMetrics[i].value);
                }
                performanceMetricsArray.push(performanceMetrics[i]);
            }
            context.commit("setPerformanceMetrics", performanceMetricsArray);
        },
        async loadPlayerData(context) {
            axios
            .get('http://0.0.0.0:5000/playerdata')
            .then(response => {
                context.commit("setPlayerData", response.data);
                let positionKeys = ["f", "d", "g"]
                for (let i = 0; i < context.state.originalTeams.length; ++i) {
                    let team = context.state.originalTeams[i]
                    let teamPlayerData = context.state.playerData[team.abbreviation];
                    let protectedMap = {}
                    let exposedMap = {}
                    positionKeys.forEach(positionKey => {
                        protectedMap[positionKey] = teamPlayerData[positionKey]
                                                    .filter(value => value.protected)
                                                    .map(function(value) {return value._id} );
                        exposedMap[positionKey] = []
                    });
                    context.commit("setOriginalTeamProtectedMap", {"protectedMap": protectedMap, "index": i});
                    context.commit("setOriginalTeamExposedMap", {"exposedMap": exposedMap, "index": i});
                }
            });
            
        },
        initialize({dispatch}) {
            dispatch('initializeTeamData');
            dispatch('initializeLoadMetrics');
            dispatch('loadPlayerData');
        },
        setCurrTeamIndex(context, index) {
            context.commit("setCurrTeamIndex", index);
        },
        setCurrFinancialMetric(context, financialMetric) {
            context.commit("setCurrFinancialMetric", financialMetric);
        },
        setCurrPerformanceMetric(context, performanceMetric) {
            context.commit("setCurrPerformanceMetric", performanceMetric);
        },
        setConsiderUFAs(context, considerUFAs) {
            context.commit("setConsiderUFAs", considerUFAs);
        },
        setExpansionTeamSliderValue(context, value) {
            context.commit("setExpansionTeamSliderValue", value);
        },
        setAllOriginalTeamsSliderValue(context, value) {
            context.commit('setAllOriginalTeamsSliderValue', value);
        },
        setOriginalTeamSliderValue(context, payload) {
            context.commit("setOriginalTeamSliderValue", payload);
        },
        setApplyToAllOriginalTeams(context, value) {
            if (value) {
                if (context.state.originalTeams) {
                    let currTeamSliderValue = context.state.originalTeams[context.state.currTeamIndex].beta;
                    context.commit('setAllOriginalTeamsSliderValue', currTeamSliderValue);
                }
            }
            context.commit("setApplyToAllOriginalTeams", value);
        },
        addToCurrTeamProtectedMap(context, payload) {
            context.commit("addToCurrTeamProtectedMap", payload);
        },
        removeFromCurrTeamProtectedMap(context, payload) {
            context.commit("removeFromCurrTeamProtectedMap", payload);
        },
        addToCurrTeamExposedMap(context, payload) {
            context.commit("addToCurrTeamExposedMap", payload);
        },
        removeFromCurrTeamExposedMap(context, payload) {
            context.commit("removeFromCurrTeamExposedMap", payload);
        }

    },
    getters: {
        getCurrTeamName : state => {
            if (state.originalTeams) {
                return state.originalTeams[state.currTeamIndex].name;
            }
            return String();
        },
        getCurrTeamAbbreviation: state => {
            if (state.originalTeams) {
                return state.originalTeams[state.currTeamIndex].abbreviation;
            }
            return String();
        },
        getCurrTeamTableData : (state, getters) => {
            let currTeamAbbreviation = getters.getCurrTeamAbbreviation
            if (currTeamAbbreviation && state.playerData)
            {
                return state.playerData[currTeamAbbreviation]
            }
            return null
        },
        getCurrFinancialMetricText: state => {
            if (state.currFinancialMetric && state.financialMetrics)
            {
                return state.financialMetrics.find(metric => metric.value == state.currFinancialMetric).text;
            }
            return String();
        },
        getCurrPerformanceMetricText: state => {
            if (state.currPerformanceMetric && state.performanceMetrics)
            {
                return state.performanceMetrics.find(metric => metric.value == state.currPerformanceMetric).text
            }
            return String();
        },
        getCurrTeamProtectedMap: state => {
            if (state.originalTeams) {
                return state.originalTeams[state.currTeamIndex].protected;
            }
            return null;
        },
        getCurrTeamExposedMap: state => {
            if (state.originalTeams) {
                return state.originalTeams[state.currTeamIndex].exposed;
            }
            return null;
        },
        getCurrTeamMeetsRequirementsMap: (state, getters) => {
            const currTeamTableData = getters.getCurrTeamTableData;
            let currTeamMeetsRequirementsMap = {}

            if (currTeamTableData)
            {
                const protectedMap = getters.getCurrTeamProtectedMap;
                const keys = Object.keys(currTeamTableData);
                keys.forEach(key => {
                    const protectedSet = new Set(protectedMap[key]);
                    currTeamMeetsRequirementsMap[key] = currTeamTableData[key].filter(player => player.meets_req && !protectedSet.has(player._id)).length;
                });
            }
            return currTeamMeetsRequirementsMap;
        }
    }
})