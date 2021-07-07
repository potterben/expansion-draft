<template>
  <b-container class ="py-4">
      <h3>{{ metricName }}</h3>
      <bar-chart v-if="dataCollection" :chart-data="dataCollection" :options="options"></bar-chart>
  </b-container>
</template>

<script>
import BarChart from '../BarChart.js'
import { mapState } from 'vuex'
export default {
    components: {
        BarChart
    },

    data: function() {
        return {
            dataCollection: null,
            options: {
                responsive: true,
                maintainAspectRatio: false,
                legend: {
                    display: false
                },
                tooltips: {
                    callbacks: {
                        label: this.formatToolTip
                    }
                }
            }
        }
    },

    props: {
        metric: String,
        metricName: String,
        isFinancial: {
            type: Boolean,
            default: false
        },
        isPerformance: {
            type: Boolean,
            default: false
        }
    },

    mounted () {
        this.fillData()
    },
    
    computed: {
        ...mapState(['figureData']),
        getFigureData() {
            return this.figureData;
        }
    },

    watch: {
        getFigureData() {
            this.fillData();
        },
        metric() {
            this.fillData();
        }
    },

    methods: {
        fillData () {
            if (this.figureData) {
                // TODO: Make this into smaller functions
                var labels = this.figureData.teamname;
                var data = this.figureData[this.metric];
                var arrayOfObj = labels.map(function(d, i) {
                    return {
                        label: d,
                        data: data[i] || 0
                    };
                });

                var sortedArrayOfObj = arrayOfObj.sort(function(a, b){
                    return b.data - a.data;
                });
                var newArrayLabel = [];
                var newArrayData = [];
                var colourArray = [];
                sortedArrayOfObj.forEach(function(d){
                    newArrayLabel.push(d.label);
                    newArrayData.push(d.data);
                    if (d.label === "SEA") {
                        colourArray.push("#99D9D9")
                    }
                    else {
                        colourArray.push("#355464")
                    }
                });

                this.dataCollection = {
                    labels: newArrayLabel,
                    datasets: 
                        [{
                            label: this.metricName,
                            backgroundColor: colourArray,
                            data: newArrayData
                        }]
                }
            }
        },
        formatToolTip (tooltipItem, data)  {
            let label = data.datasets[tooltipItem.datasetIndex].label || '';
            if (label) {
                label += ': ';
                if (this.isFinancial) {
                    label += "$" + tooltipItem.yLabel.toFixed(3) + "M";
                } else {
                    label += tooltipItem.yLabel.toFixed(2);
                }
            } 
            return label;
        }
    }
}
</script>
