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
                            <b-form-select v-model="financialMetric" :options="this.financialMetrics"></b-form-select>
                        </b-col>
                        <b-col>
                            <b-form-select v-model="performanceMetric" :options="this.performanceMetrics"></b-form-select>
                        </b-col>
                    </b-row>
                    <b-row>
                        <b-col>
                            <b-form-checkbox id ="ufa" v-model="considerUFAState">
                                Don't Consider UFAs
                            </b-form-checkbox>
                        </b-col>
                        <b-col/>
                    </b-row>
                    <TeamSlider :teamName="expansionTeam.name" :isExpansionTeam="true" v-if="expansionTeam" />
                    <TeamSlider :teamName="currTeam.name" v-if="currTeam"/>
                </b-container>
            </b-modal>
        </b-container>
    </footer>
</template>

<script>
import TeamSlider from './TeamSlider.vue'
import { mapState, mapActions } from 'vuex'

export default {
    name: 'FooterArea',

    components: {
        TeamSlider
    },

    computed: {
        financialMetric: {
            get() {
                return this.currFinancialMetric;
            },
            set(value) {
                this.setCurrFinancialMetric(value);
            }
        },
        performanceMetric: {
            get() {
                return this.currPerformanceMetric;
            },
            set(value) {
                this.setCurrPerformanceMetric(value);
            }
        },
        considerUFAState: {
            get() {
                return this.considerUFAs;
            },
            set(value) {
                this.setConsiderUFAs(value);
            }
        },
        ...mapState([
            'currFinancialMetric',
            'financialMetrics',
            'currPerformanceMetric',
            'performanceMetrics',
            'expansionTeam',
            'currTeam',
            'considerUFAs'
        ])
    },

    methods: {
        handleCheckbox: function ()
        {
           console.log("Changed!");

        },
        ...mapActions([
            'setCurrFinancialMetric',
            'setCurrPerformanceMetric',
            'setConsiderUFAs'
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
