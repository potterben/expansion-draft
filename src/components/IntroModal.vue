<template>
    <b-modal ref="intro-modal">
        <div class="d-block text-center">
            <h3>Introduction Modal!</h3>
        </div>
        <template #modal-footer>
            <b-form-checkbox
            v-model="doNotShowIntroModal"
            value="checked"
            unchecked-value="unchecked"
            >
                Do not show this dialog again
            </b-form-checkbox>
        </template>
    </b-modal>
</template>

<script>
export default {
    name: 'IntroModal',

    data() {
        return {
            doNotShowIntroModal: "unchecked"
        }
    },

    mounted() {
        if (localStorage.doNotShowIntroModal) {
            this.doNotShowIntroModal = localStorage.doNotShowIntroModal;
        }
        if (this.doNotShowIntroModal == "unchecked") {
            this.showModal();
        }
    },

    watch: {
        doNotShowIntroModal(value) {
            localStorage.doNotShowIntroModal = value;
        }
    },

    components: {

    },

    computed: {
       
    },

    methods: {
        showModal() {
            this.$refs['intro-modal'].show()
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
