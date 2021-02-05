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

export default {
  name: 'App',
  components: {
    HeaderArea,
    MainArea,
    FooterArea
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
