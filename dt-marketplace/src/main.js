import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import antd from "./antd";
import VueClipboard2 from "vue-clipboard2";

import "./styles/base.less";

Vue.config.productionTip = false;

Vue.use(antd);
Vue.use(VueClipboard2);

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
