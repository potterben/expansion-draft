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
        this.protected = null;
        this.exposed = null;
        this.beta = 0.0;
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

class ComboBoxOption {
    constructor(text, value) {
        this.text = text;
        this.value = value;
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

        allTeams: [],

        currFinancialMetric: "",
        financialMetrics: [],

        currPerformanceMetric: "",
        performanceMetrics: [],

        considerUFAs: false,
        applyToAllOriginalTeams: true,
        playerData: [],
        positionKeys: ["forwards", "defensemen", "goalies"]

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
        setAllTeams(state, allTeams) {
            state.allTeams = allTeams;
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
            state.originalTeams[state.currTeamIndex].protected[payload.position].push(payload.id);
        },
        removeFromCurrTeamProtectedMap(state, payload) {
            const updatedArray = removeFromArray(state.originalTeams[state.currTeamIndex].protected[payload.position], payload.id);
            state.originalTeams[state.currTeamIndex].protected[payload.position] = updatedArray;
        },
        setOriginalTeamExposedMap(state, payload) {
            state.originalTeams[payload.index].exposed = payload.exposedMap;
        },
        addToCurrTeamExposedMap(state, payload) {
            state.originalTeams[state.currTeamIndex].exposed[payload.position].push(payload.id);
        },
        removeFromCurrTeamExposedMap(state, payload) {
            const updatedArray = removeFromArray(state.originalTeams[state.currTeamIndex].exposed[payload.position], payload.id);
            state.originalTeams[state.currTeamIndex].exposed[payload.position] = updatedArray;
        },
        addToCurrTeamDoesNotMeetProtectReqs(state, position) {
            state.originalTeams[state.currTeamIndex].doesNotMeetProtectReqs.push(position);
        },
        removeFromCurrTeamDoesNotMeetProtectReqs(state, position) {
            const updatedArray = removeFromArray(state.originalTeams[state.currTeamIndex].doesNotMeetProtectReqs, position);
            state.originalTeams[state.currTeamIndex].doesNotMeetProtectReqs = updatedArray;
        },
        addToCurrTeamDoesNotMeetExposeReqs(state, position) {
            state.originalTeams[state.currTeamIndex].doesNotMeetExposeReqs.push(position);
        },
        removeFromCurrTeamDoesNotMeetExposeReqs(state, position) {
            const updatedArray = removeFromArray(state.originalTeams[state.currTeamIndex].doesNotMeetExposeReqs, position);
            state.originalTeams[state.currTeamIndex].doesNotMeetExposeReqs = updatedArray;
        }
      },
    actions: {
        initializeTeamData(context) {
            let allTeamsArray = [];
            let originalTeams = TeamInfoJson.originalTeams;
            let originalTeamsArray = []
            
            for (let i =0; i < originalTeams.length; i++) {
                originalTeamsArray.push(new OriginalTeam(originalTeams[i].name,originalTeams[i].abbreviation, i));
                allTeamsArray.push(new ComboBoxOption(originalTeams[i].name, i));
            }
            context.commit("setOriginalTeams", originalTeamsArray);

            let expansionTeam = TeamInfoJson.expansionTeam;
            let expansionTeamObject = new ExpansionTeam(expansionTeam[0].name, expansionTeam[0].abbreviation);
            allTeamsArray.unshift(new ComboBoxOption(expansionTeamObject.name, originalTeams.length));

            context.commit("setExpansionTeam", expansionTeamObject);
            context.commit("setAllTeams", allTeamsArray)
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
            .get('http://0.0.0.0:8000/data')
            .then(response => {
                context.commit("setPlayerData", response.data);

                for (let i = 0; i < context.state.originalTeams.length; ++i) {
                    let teamPlayerData = context.state.playerData[i];
                    let protectedMap = {}
                    let exposedMap = {}
                    context.state.positionKeys.forEach(positionKey => {
                        protectedMap[positionKey] = teamPlayerData[positionKey]
                                                    .filter(value => value.nmc)
                                                    .map(function(value) {return value.id} );
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
        },
        optimize(context) {
            return new Promise((resolve, reject) => {
                const payload = {
                    original_teams: context.state.originalTeams,
                    financial_metric: context.state.currFinancialMetric,
                    performance_metric: context.state.currPerformanceMetric,
                    alpha: context.state.expansionTeam.alpha
                };
                const headers = {
                    'Access-Control-Allow-Origin': '*'
                  }
                axios
                .post('http://0.0.0.0:8000/optimize/', payload, { 'headers': headers})
                .then(response => {
                    let results = response.data
                    let originalTeamsResults = results["original_teams"]
                    for (let i = 0; i < originalTeamsResults.length; ++i) {
                        let teamResults = originalTeamsResults[i];
                        let protectedMap = {}
                        context.state.positionKeys.forEach(positionKey => {
                            protectedMap[positionKey] = teamResults[positionKey].map(function(value) {return value.id} );
                        });
                        context.commit("setOriginalTeamProtectedMap", {"protectedMap": protectedMap, "index": i});
                    }
                    resolve(response);
                }, error => {
                    // http failed, let the calling function know that action did not work out
                    reject(error);
                    console.log(error)
                })
            })
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
        getCurrTeamTableData : state => {
            if (state.originalTeams && state.playerData) {
                return state.playerData[state.currTeamIndex]
            }
            return [];
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
                state.positionKeys.forEach(position => {
                    const protectedSet = new Set(protectedMap[position]);
                    currTeamMeetsRequirementsMap[position] = currTeamTableData[position].filter(player => player.meets_req && !protectedSet.has(player._id)).length;
                });
            }
            return currTeamMeetsRequirementsMap;
        },
        getForwardsString: state => {
            return state.positionKeys[0];
        },
        getDefensemenString: state => {
            return state.positionKeys[1];
        },
        getGoaliesString: state => {
            return state.positionKeys[2];
        }
    }
})