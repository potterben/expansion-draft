<template>
    <b-form-checkbox :checked="isChecked" @change="onChange($event, position, id)" :disabled="isDisabled"></b-form-checkbox>
</template>

<script>
export default {
    name: 'TableCheckbox',

    props: {
        id: String,
        position: String,
        checkedMap: Object,
        onChange: Function,
        isTableDisabled: Function
    },

    computed: {
        isChecked() {
            return this.checkedMap[this.position].indexOf(this.id) > -1 ;
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