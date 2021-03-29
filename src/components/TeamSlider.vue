<template>
    <div class="m-4 p-2" id="parameter-center">
        <b-row class="justify-content-center">
            <b-col>
                <h4>
                    {{ teamName }}
                </h4>
            </b-col>
        </b-row>
        <b-row class="justify-content-center">
            <b-col cols=6>
                <vue-slider v-model="sliderValue" />
            </b-col>
            </b-row>
        <b-row class="justify-content-center">
            <b-col>
                <label class="p-2" for="financial_flexiblity">
                    Financial Flexibility:
                </label>
                <input type="number" min="0" max="100" name="financial_flexiblity" id="financial_flexiblity" v-model="sliderValue">%
            </b-col>
            <b-col>
                <label class="p-2" for="on_ice_performance">On-Ice Performance:</label>
                <input type="number" min="0" max="100" name="on_ice_performance" id="on_ice_performance" v-model="invertedPercentageValue">%
            </b-col>
        </b-row>
    </div>
</template>

<script>
import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/antd.css'
import { mapState, mapActions } from 'vuex'

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
        }
    },

    computed: {
        invertedPercentageValue: {
            get() {
                return (100-this.sliderValue);
            },
            set(newVal) {
                this.sliderValue = newVal;
            }
        },
        sliderValue: {
            get() {
                if (this.isExpansionTeam) {
                    return this.expansionTeam ? this.expansionTeam.alpha : 0;
                }
                else {
                    return this.currTeam ? this.currTeam.beta : 0;
                }
            },
            set(value) {
                if (this.isExpansionTeam) {
                    this.setExpansionTeamSliderValue(value);
                }
                else {
                    this.setCurrTeamSliderValue(value);
                }
            }
        },
        ...mapState([
            'expansionTeam',
            'currTeam'
        ])
    },

    methods: {
        ...mapActions([
            'setExpansionTeamSliderValue',
            'setCurrTeamSliderValue'
        ])
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
