<template>
    <b-form-checkbox :checked="isChecked" @change="onChange($event, positionId, id)" :disabled="isDisabled"></b-form-checkbox>
</template>

<script>
export default {
    name: 'TableCheckbox',

    props: {
        id: String,
        positionId: String,
        checkedMap: Object,
        onChange: Function,
        isTableDisabled: Function
    },

    computed: {
        isChecked() {
            return this.checkedMap[this.positionId].indexOf(this.id) > -1 ;
        },
        isDisabled() {
            if (!this.isChecked && this.isTableDisabled) {
                    return this.isTableDisabled();
                }
            else {
                return false;
            }
        }
    }
}
</script>