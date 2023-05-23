import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/MovieView'
import HomeView from '@/views/HomeView'
import TestView from '@/views/test'
import SignUpView from '@/views/SignUpView'
import LoginView from '@/views/LoginView'
import SearchMovieView from '@/views/SearchMovieView'
import DetailMovieView from '@/views/DetailMovieView'

import UpdateProfileView from '@/views/UpdateProfileView'
import MyContentView from '@/views/MyContentView'
import ProfileView from '@/views/ProfileView'
import ArticleView from '@/views/ArticleView'
import ArticleDetailView from '@/views/ArticleDetailView'
import ArticleCreateView from '@/views/ArticleCreateView'
Vue.use(VueRouter)

const routes = [
  {
    path: '/movies/:page',
    name: 'MovieView',
    component: MovieView
  },
  {
    path: '/articles',
    name: 'ArticleView',
    component: ArticleView
  },
  {
    path: '/articles/:articleId',
    name: 'ArticleDetailView',
    component: ArticleDetailView
  },
  {
    path: '/articles/create',
    name: 'ArticleCreateView',
    component: ArticleCreateView
  },
  {
    path: '/updateprofile/',
    name: 'UpdateProfileView',
    component: UpdateProfileView
  },
  {
    path: '/profile',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/movies/detail/:movieId',
    name: 'DetailMovieView',
    component: DetailMovieView
  },
  {
    path: '/movies/mycontent/',
    name: 'MyContentView',
    component: MyContentView
  },
  {
    path: '/test',
    name: 'TestView',
    component: TestView
  },
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/search/keyword=:keyword',
    name: 'SearchMovieView',
    component: SearchMovieView
  },
  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  // }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
