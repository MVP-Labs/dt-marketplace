import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/home/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/detail/:dt",
    name: "Detail",
    component: () =>
      import(/* webpackChunkName: "detail" */ "../views/detail/Detail.vue"),
  },
];

const router = new VueRouter({
  routes,
});

export default router;
