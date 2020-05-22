// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css';
import axios from 'axios';
import moment from 'moment'
import store from './store'
import echarts from 'echarts'
Vue.prototype.$axios = axios;
axios.interceptors.request.use((config) => {
  config.headers['X-Requested-With'] = 'XMLHttpRequest';
  let regex = /.*csrftoken=([^;.]*).*$/; // 用于从cookie中匹配 csrftoken值
  config.headers['X-CSRFToken'] = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1];
  return config
 });
//Vue.prototype.$host ='http://127.0.0.1:8000/'
Vue.prototype.$host ='http://121.199.23.195:8000/'
Vue.config.productionTip = false
Vue.use(ElementUI);
Vue.prototype.$echarts = echarts
/* eslint-disable no-new */
//全局过滤器
Vue.prototype.$moment = moment;
Vue.filter('dateFmt', (input, formatString = "YYYY-MM-DD hh:mm:ss") => {
    //es5函数参数设置默认值
    //const lastFormatString = formatString ||


     // moment(input) 把时间字符串转成时间对象
     // format(formatString) 把时间对象，按照指定格式，格式化成符合条件的字符串
    return moment(input).format(formatString)
})

new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
