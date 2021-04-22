<template>
    <div>
        <HeaderArea />
        <MainArea />
        <FooterArea />
    </div>
</template>

<script>
import HeaderArea from './components/HeaderArea.vue'
import MainArea from './components/MainArea.vue'
import FooterArea from './components/FooterArea.vue'
import { mapActions } from 'vuex'


export default {
    name: 'App',

    components: {
        HeaderArea,
        MainArea,
        FooterArea
    },

    methods: {
        ...mapActions([
            'initialize',
            'loadPlayerData'
        ])
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
