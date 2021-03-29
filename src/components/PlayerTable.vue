<template>
    <b-container>
        <h3>
            {{positionTitle}}
        </h3>
        <b-table-simple class='table table-hover table-striped table-team sticky-header'>
            <b-thead>
                <b-tr>
                    <b-th>Protect</b-th>
                    <b-th>Expose</b-th>
                    <b-th>Name</b-th>
                    <b-th>Age</b-th>
                    <b-th>Pos.</b-th>
                    <b-th :class="currFinancialMetric">
                        {{currFinancialMetric}}
                    </b-th>
                    <b-th :class="currPerformanceMetric">
                        {{currPerformanceMetric}}
                    </b-th>
                    <b-th>Expiry</b-th>
                    <b-th>Exposure Req. Met</b-th>
                </b-tr>
            </b-thead>
            <b-tbody :id ="positionId">
            </b-tbody>
        </b-table-simple>
    </b-container>
</template>

<script>
import { mapState } from 'vuex'

export default {
    name: 'PlayerTable',

    props: {
        positionTitle: String,
        positionId: String
    },

    computed: {
        ...mapState([
            'currFinancialMetric',
            'currPerformanceMetric'
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
a {
    color: #42b983;
}
</style>
