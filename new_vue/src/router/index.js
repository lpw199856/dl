import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/home'
import login from '@/components/login'
import test1 from '@/components/test1'
import digits from '@/components/digits'
import letter from '@/components/letter'
import statistics from '@/components/statistics'
Vue.use(Router)
const router=new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: home,
      children:[
         {
            path:'digits',
            component: digits
          },
        {
          path:'letter',
          component:letter
        },
        {
      path: 'statistics',
      component: statistics,
      },
        {
          path:'/',
          component:test1,
        },
      ]
    },
    {
      path: '/login',
      name: 'login',
      component: login,
    },

  ]
})
router.beforeEach((to, from, next) => {
  if (to.path === '/login') {
    next();
  } else {
    let token = localStorage.getItem('Authorization');
    let loginon =localStorage.getItem('loginon');
    console.log(loginon)
    console.log(token)
    if (loginon == 'false' || token == null) {
      next('/login');
    } else {
      next();
    }
  }
});
export default router;
