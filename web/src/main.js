import Vue from 'vue'
import App from './App.vue'

import {
  MdApp,
  MdLayout,
  MdContent,
  MdAutocomplete,
  MdMenu,
  MdField,
  MdList,
  MdButton,
  MdCard,
  MdBadge
} from 'vue-material/dist/components'

import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

Vue.use(MdApp)
Vue.use(MdLayout)
Vue.use(MdContent)
Vue.use(MdAutocomplete)
Vue.use(MdMenu)
Vue.use(MdField)
Vue.use(MdList)
Vue.use(MdButton)
Vue.use(MdCard)
Vue.use(MdBadge)

// configure vue router (https://router.vuejs.org/installation.html)
import VueRouter from 'vue-router'

Vue.use(VueRouter)

// configure the app's routing
import PackageSearch from '@/pages/PackageSearch.vue'

const routes = [
  { path: '/', component: PackageSearch }
]

const router = new VueRouter({
  routes
})

// configure the store
import store from '@/store'

Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app')
