import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Antdv from './antdv'

import './styles/index.less'

Vue.config.productionTip = false

Vue.use(Antdv)

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app')
