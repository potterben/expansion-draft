<template>
    <b-form-checkbox :checked="isProtected" @change="onChange($event, positionId, id), $emit('TableCheckboxChanged')"></b-form-checkbox>
</template>

<script>
export default {
    name: 'TableCheckbox',

    props: {
        id: String,
        positionId: String,
        checkedMap: Object,
        onChange: Function
    },

    computed: {
        isProtected() {
            return this.checkedMap[this.positionId].indexOf(this.id) > -1 ;
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
