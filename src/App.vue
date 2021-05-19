<template>
  <div>
    <HeaderArea/>
    <router-view/>
  </div>
</template>
<script>
import HeaderArea from './components/HeaderArea.vue'

export default {
  name: 'App',
  components: {
    HeaderArea
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
