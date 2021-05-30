<template>
    <div>
        <IntroModal/>
        <MainArea />
        <FooterArea />
    </div>
</template>

<script>
import IntroModal from '../components/IntroModal.vue'
import MainArea from '../components/MainArea.vue'
import FooterArea from '../components/FooterArea.vue'

export default {
    name: 'Home',

    components: {
        IntroModal,
        MainArea,
        FooterArea
    }
}
</script>

<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
</style>