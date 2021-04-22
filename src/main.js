import Vue from 'vue'

import App from './App.vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import './styles/_main.scss'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)


import store from '../store'

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
	render(h) {
		if (this.isInitialized) {
			return h(App)
		}
		else {
			return null;
		}
	}
})
