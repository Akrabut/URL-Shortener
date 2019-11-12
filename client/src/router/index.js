import Vue from 'vue';
import VueRouter from 'vue-router';
import Statistics from '../components/Statistics.vue';
import Home from '../components/Home.vue';
import NotFound from '../components/NotFound.vue';

Vue.use(VueRouter);

// home contains the url shortening form, stats contains the statistics and
// notfound contains... well, nothing
const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/stats',
    name: 'statistics',
    component: Statistics,
  },
  {
    path: '*',
    name: 'notfound',
    component: NotFound,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
