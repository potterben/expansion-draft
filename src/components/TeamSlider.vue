<template>
    <div class="m-4 p-2" id="parameter-center">
        <b-row class="justify-content-center">
            <b-col>
                <h4>
                    {{ teamName }}
                </h4>
            </b-col>
        </b-row>
        <b-row class="justify-content-center py-3">
            <b-col cols=6>
                <vue-slider class="" v-model="sliderValue" :lazy="true" :tooltip="'none'" @change="handleChange"/>
            </b-col>
            </b-row>
        <b-row class="justify-content-center py-3">
            <b-col>
                <label class="p-2" for="on_ice_performance">
                    {{ getCurrPerformanceMetricText }}:
                </label>
                <input class="percentage" type="number" min="0" max="100" name="on_ice_performance" id="on_ice_performance" v-model="invertedPercentageValue"> %
            </b-col>
            <b-col>
                <label class="p-2" for="financial_flexiblity">
                    {{ getCurrFinancialMetricText }}:
                </label>
                <input class="percentage" type="number" min="0" max="100" name="financial_flexiblity" id="financial_flexiblity" v-model="sliderValue"> %
            </b-col>
        </b-row>
    </div>
</template>

<script>
import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/antd.css'
import { mapState, mapActions, mapGetters } from 'vuex'

export default {
    name: 'TeamSlider',

    components: {
        VueSlider
    },

    props: {
        isExpansionTeam: {
            type: Boolean,
            default: false
        },
        teamName: {
            type: String
        },
        teamIndex: {
            type: Number,
            default: -1
        },
        onChange: Function
    },

    computed: {
        invertedPercentageValue: {
            get() {
                return 100-this.sliderValue;
            },
            set(newVal) {
                this.sliderValue = 100-newVal;
            }
        },
        sliderValue: {
            get() {
                if (this.isExpansionTeam) {
                    return this.expansionTeam ? this.expansionTeam.alpha : 0;
                }
                else {
                    if (this.teamIndex == -1) {
                        return this.originalTeams.length ? this.originalTeams[this.currTeamIndex].beta : 0;
                    }
                    else {
                        return this.originalTeams.length ? this.originalTeams[this.teamIndex].beta : 0;
                    }
                }
            },
            set(value) {
                if (this.isExpansionTeam) {
                    this.setExpansionTeamSliderValue(value);
                }
                else {
                    if (this.teamIndex == -1) {
                        this.setAllOriginalTeamsSliderValue(value);
                    }
                    else {
                        let payload = {
                            value: value,
                            index: this.teamIndex
                        }
                        this.setOriginalTeamSliderValue(payload);
                    }
                }
            }
        },
        ...mapState([
            'expansionTeam',
            'currTeamIndex',
            'originalTeams',
            'applyToAllOriginalTeams'
        ]),
        ...mapGetters([
            'getCurrPerformanceMetricText',
            'getCurrFinancialMetricText'
        ])
    },

    methods: {
        handleChange() {
            if (typeof this.onChange === 'function'){
                this.onChange(this);
            }
        },
        ...mapActions([
            'setExpansionTeamSliderValue',
            'setAllOriginalTeamsSliderValue',
            'setOriginalTeamSliderValue'
        ])
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
