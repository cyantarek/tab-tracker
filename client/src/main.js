// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import { sync } from 'vuex-router-sync'
import store from '@/store/store'
import VueYoutubeEmbed from 'vue-youtube-embed'
import Panel from '@/components/Base/Panel'

sync(store, router)

Vue.config.productionTip = false
Vue.use(Vuetify)

Vue.use(VueYoutubeEmbed)

Vue.component('panel', Panel)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
