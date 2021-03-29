import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import TeamInfoJson from './data/TeamsInfo.json'
import MetricsInfoJson from './data/MetricsInfo.json'

Vue.use(Vuex)

// TODO: seperate into separate files
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
        this.protected = [];
        this.exposed = [];
        this.beta = 1.0;
        this.constraints = {'f_p': 0, 'f_e': 0, 'd_p': 0, 'd_e': 0, 'g_p': 0, 'g_e': 0}
    }    
}

class ExpansionTeam extends Team {
    constructor(name, abbreviation) {
        super(name, abbreviation);
        this.keep = [];
        this.remove = [];
        this.alpha = 1.0;
    }    
}

export default new Vuex.Store({
    state: {
        currTeam: null,
        originalTeams: [],

        currFinancialMetric: "",
        financialMetrics: [],

        currPerformanceMetric: "",
        performanceMetrics: [],
        
        consider_ufas: false,
        
        expansionTeam: null,
        
        playerData: []
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
        },
        setFinancialMetrics(state, financialMetrics) {
            state.financialMetrics = financialMetrics;
        },
        setPerformanceMetrics(state, performanceMetrics) {
            state.performanceMetrics = performanceMetrics;
        },
        setOriginalTeams(state, originalTeams) {
            state.originalTeams = originalTeams;
        },
        setExpansionTeam(state, expansionTeam) {
            state.expansionTeam = expansionTeam;
        },
        setPlayerData(state, playerData) {
            state.playerData = playerData;
        }
      },
    actions: {
        setCurrTeam(context, index) {
            let team = context.state.originalTeams[index];
            context.commit("setCurrTeam", team);
        },
        setCurrFinancialMetric(context, financialMetric) {
            context.commit("setCurrFinancialMetric", financialMetric);
        },
        setCurrPerformanceMetric(context, performanceMetric) {
            context.commit("setCurrPerformanceMetric", performanceMetric);
        },
        initializeTeamData(context) {
            let expansionTeam = TeamInfoJson.expansionTeam;
            let expansionTeamObject = new ExpansionTeam(expansionTeam[0].name, expansionTeam[0].abbreviation);
            context.commit("setExpansionTeam", expansionTeamObject);

            let originalTeams = TeamInfoJson.originalTeams;
            let originalTeamsArray = []
            for (let i =0; i < originalTeams.length; i++) {
                let teamToAdd = new OriginalTeam(originalTeams[i].name,originalTeams[i].abbreviation, i);
                if (i==0) {
                    context.commit("setCurrTeam", teamToAdd);
                }
                originalTeamsArray.push(teamToAdd);
            }
            context.commit("setOriginalTeams", originalTeamsArray);
        },
        initializeLoadMetrics(context) {
            let financialMetrics = MetricsInfoJson.financialMetrics;
            let financialMetricsArray = [];
            for (let i =0; i < financialMetrics.length; i++)
            {
                if (i==0) {
                    context.commit("setCurrFinancialMetric", financialMetrics[i].value);
                }
                financialMetricsArray.push(financialMetrics[i]);
            }
            context.commit("setFinancialMetrics", financialMetricsArray);
            
            let performanceMetrics = MetricsInfoJson.performanceMetrics
            let performanceMetricsArray = []
            for (let i =0; i < performanceMetrics.length; i++)
            {
                if (i==0) {
                    context.commit("setCurrPerformanceMetric", performanceMetrics[i].value);
                }
                performanceMetricsArray.push(performanceMetrics[i]);
            }
            context.commit("setPerformanceMetrics", performanceMetricsArray);
        },
        async loadPlayerData(context) {
            axios
            .get('http://0.0.0.0:5000/data')
            .then(response => (context.commit("setPlayerData", response.data)))
        },
        initialize({dispatch}) {
            dispatch('initializeTeamData');
            dispatch('initializeLoadMetrics');
        }
    }
})