<template>
    <b-form-checkbox :checked="isProtected" @change="checkboxChanged"></b-form-checkbox>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
    name: 'ProtectedCheckbox',

    props: {
        id: String,
        positionId: String
    },

    computed: {
        ...mapGetters([
            'getCurrTeamProtectedMap'
        ]),
        isProtected() {
            return this.getCurrTeamProtectedMap[this.positionId].indexOf(this.id) > -1 ;
        }
    },

    methods: {
        checkboxChanged(value) {
            let payload = {
                "positionId": this.positionId,
                "id": this.id
            }
            if (value) {
                this.addToCurrTeamProtectedMap(payload);
            }
            else {
                this.removeFromCurrTeamProtectedMap(payload);
            }
        },
        ...mapActions([
            'addToCurrTeamProtectedMap',
            'removeFromCurrTeamProtectedMap'
        ])
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
