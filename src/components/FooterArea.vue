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
                            <b-form-select v-model="financial_metric" :options="metrics.financial_metric"></b-form-select>
                        </b-col>
                        <b-col>
                            <b-form-select v-model="performance_metric" :options="metrics.performance_metric"></b-form-select>
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
import { mapState, mapGetters, mapActions } from 'vuex'

export default {
    name: 'FooterArea',

    components: {
        TeamSlider
    },

    inject : [
        'metrics'
    ],

    data () {
        return {
            value: 0
        }
    },

    computed: {
        financial_metric:{
            get() {
                return this.currFinancialMetric;
            },
            set(value) {
                this.setCurrFinancialMetric(value);
            }
        },
        performance_metric: {
            get() {
                return this.currPerformanceMetric;
            },
            set(value) {
                this.setCurrPerformanceMetric(value);
            }
        },
        ...mapGetters([
            'getCurrTeamName',
        ]),
        ...mapState([
            'currPerformanceMetric',
            'currFinancialMetric'
        ])
    },

    created() {
        this.setCurrFinancialMetric(this.metrics.financial_metric[0].value);
        this.setCurrPerformanceMetric(this.metrics.performance_metric[0].value);
    },

    methods: {
        ...mapActions([
            'setCurrFinancialMetric',
            'setCurrPerformanceMetric'
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
