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
  MdButton
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

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
