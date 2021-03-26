<template>
    <div class="m-4 p-2" id="parameter-center">
        <b-row class="justify-content-center">

        </b-row>
        <b-row class="justify-content-right" >
            <b-col cols=4>
               
            </b-col>
        </b-row>
        <b-row class="justify-content-center">
            <b-col>
              <h4>{{ team_name }}</h4>
            </b-col>
        </b-row>
        <b-row class="justify-content-center">
          <b-col cols=6 >
            <vue-slider v-model="sliderValue" />
          </b-col>
        </b-row>
        <b-row class="justify-content-center">
            <b-col>
                <label class="p-2" for="financial_flexiblity">Financial Flexibility:</label>
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

export default {
  name: 'TeamSlider',
  components: {
    VueSlider
  },
  props: {
    team_name: {
       type: String,
       default: "Seattle Kraken"
    }
  },
  data () {
    return {
      sliderValue: 0
    }
  },
   computed: {

    invertedPercentageValue: {
        get(){
            //this function will determine what is displayed in the input
            return 100-this.sliderValue;
        },
        set(newVal){
            //this function will run whenever the input changes
            this.sliderValue = newVal;
        }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
