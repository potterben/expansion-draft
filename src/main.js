import Vue from 'vue'

import App from './App.vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import VueLoading from 'vuejs-loading-plugin'

import './styles/_main.scss'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

Vue.use(VueLoading, {
	background: 'rgb(255,255,255, 0.9)',
  })

import store from '../store'
import router from './router'

Vue.config.productionTip = false

new Vue({
    el: '#app',
    store,

    data() {
		return {
			isInitialized: false
		}
	},

    async beforeCreate() {
		await this.$store.dispatch("initialize");
		this.isInitialized = true;
	},

    router,

    render(h) {
		if (this.isInitialized) {
			return h(App)
		}
		else {
			return null;
		}
	}
})
