<template>
    <div>
        <h3>{{position_title}}</h3>
        <table class='table table-hover table-striped table-team sticky-header'>
            <thead>
                <tr>
                    <th>Protect</th>
                    <th>Expose</th>
                    <th>Name</th>
                    <th>Age</th>
                    <th>Pos.</th>
                    <th class = "ea_rating">EA Rating</th>
                    <th class = "ps_14_15">PS (14/15)</th>
                    <th class = "ps_15_16">PS (15/16)</th>
                    <th class = "gaps_16_17">Adjusted PS (16/17)</th>
                    <th class = "gaps_15_16">Adjusted PS (15/16)</th>
                    <th class = "gaps_14_15">Adjusted PS (14/15)</th>
                    <th class = "ps_avg">Avg. PS</th>
                    <th class = "gvt_avg">Avg. GVT</th>
                    <th class = "ps_16_17">PS (16/17)</th>
                    <th class = "gvt_14_15">GVT (14/15)</th>
                    <th class = "gvt_15_16">GVT (15/16)</th>
                    <th class="cap_hit_17_18">Cap Hit (17/18)</th>
                    <th class="cap_hit_total">Cap Hit '17 On</th>
                    <th>Expiry</th>
                    <th>Exposure Req. Met</th>
                </tr>
            </thead>
            <tbody v-bind:id ="position_id">
            </tbody>
        </table>
        </div>
</template>

<script>
export default {
  name: 'PlayerTable',
  props: {
    position_title: String,
    position_id: String
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
a {
  color: #42b983;
}
</style>
