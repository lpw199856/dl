import Vue from 'vue'
import Vuex from 'vuex'

//挂载Vuex
Vue.use(Vuex)

//创建VueX对象
const store = new Vuex.Store({
    state:{
        // 存储token
    Authorization: localStorage.getItem('Authorization') ? localStorage.getItem('Authorization') : '',
      Authorization2: localStorage.getItem('Authorization2') ? localStorage.getItem('Authorization2') : '',
    loginon: localStorage.getItem('loginon') ? localStorage.getItem('loginon') : 'false',
    },
  mutations: {
    // 修改token，并将token存入localStorage
    changeLogin (state, user) {
      state.Authorization = user.Authorization;
      state.Authorization2 = user.Authorization2;
      state.loginon = user.loginon;
      localStorage.setItem('Authorization', user.Authorization);
      localStorage.setItem('Authorization2', user.Authorization2);
      localStorage.setItem('loginon',user.loginon);
    }
  }
})

export default store
