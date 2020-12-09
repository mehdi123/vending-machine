import Vue from 'vue'
import App from '@/App.vue'

import store from '@/store' 
import router from '@/router'

import SuiVue from 'semantic-ui-vue';
import 'semantic-ui-css/semantic.min.css';

Vue.config.productionTip = false
Vue.use(SuiVue);

// Vue.use(VueRouter)

const vue = new Vue({
  router,
  store,
  render: h => h(App)
})

vue.$mount('#app');
