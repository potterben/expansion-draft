<template>
    <div class="m-4 p-2" id="parameter-center">
        <div class="row justify-content-end" v-if="team_name == null">
            <div class="col-4">
            Seattle Kraken
            </div>
            <div class="col-4">
                <input type="checkbox" id ="ufa">Don't Consider UFAs
            </div>
        </div>
        <div class="row justify-content-center" v-else>
            <div class="col-4">
            {{ team_name }}
            </div>
        </div>
        <div class="row justify-content-center">
            <div class="col-4">
                <vue-slider v-model="value" />
            </div>
        </div>
        <div class="row justify-content-between">
            <div class="col-4">
                <label for="financial_flexiblity">Financial Flexibility:</label>
                <input type="number" name="financial_flexiblity" id="financial_flexiblity" value="0">
            </div>
            <div class="col-4">
                <label for="on_ice_performance">On-Ice Performance:</label>
                <input type="number" name="on_ice_performance" id="on_ice_performance" value="100">
            </div>
        </div>
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
       default: null
    }
  },
  data () {
    return {
      value: 0
    }
  }  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<!-- Add padding  -->
<style scoped>
b-container {

}
</style>
