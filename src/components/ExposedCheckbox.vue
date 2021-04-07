<template>
    <b-form-checkbox :checked="isExposed" @change="checkboxChanged"></b-form-checkbox>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
    name: 'ExposedCheckbox',

    props: {
        id: String,
        positionId: String
    },

    computed: {
        ...mapGetters([
            'getCurrTeamExposedMap'
        ]),
        isExposed() {
            return this.getCurrTeamExposedMap[this.positionId].indexOf(this.id) > -1 ;
        }
    },

    methods: {
        checkboxChanged(value) {
            let payload = {
                "positionId": this.positionId,
                "id": this.id
            }
            if (value) {
                this.addToCurrTeamExposedMap(payload);
            }
            else {
                this.removeFromCurrTeamExposedMap(payload);
            }
        },
        ...mapActions([
            'addToCurrTeamExposedMap',
            'removeFromCurrTeamExposedMap'
        ])
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
