import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'

import createPersistedState from 'vuex-persistedstate'
Vue.use(Vuex)


const API_URL = 'http://127.0.0.1:8000'
export default new Vuex.Store({
  plugins:[
    createPersistedState()
  ],
  state: {
    movies : [],
    token : null,
    likeMovies: [],
    wishMovies:[]
  },
  getters: {
  },
  mutations: {
    SAVE_TOKEN(state, token){
      state.token = token
      router.push({name:'MovieView'})
    },
    LIKE_MOVIE(state, movie){
      state.likeMovies.push(movie)
    },
    WISH_MOVIE(state,movie){
      state.wishMovies.push(movie)
    }
  },
  actions: {

    signUp(context,payload){
      const username = payload.username
      const email = payload.email
      const password1 = payload.password1
      const password2 = payload.password2
      axios({
        method: 'post',
        url : `${API_URL}/accounts/signup/`,
        data : {
          username, email, password1,password2
        }
      })
      .then((response)=>{
        context.commit('SAVE_TOKEN', response.data.key)
      })
      .catch((err)=>{
        console.log(err)
      })
      
    },
    login(context,payload){
      const email = payload.email
      const password = payload.email

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data : {
          email,password
        }
      })
      .then((response)=>{
        context.commit('SAVE_TOKEN',response.data.key)
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    likeMovie(context,movieId){
      axios({
        method:'post',
        url: `${API_URL}/movies/${movieId}/likes/`,
        //가정
        headers: {Authorization: `Token ${localStorage.getItem('token')}`}
      })
      .then((response)=>{
        context.commit('LIKE_MOVIE', response.data)
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    wishMovie(context,movieId){
      axios({
        method: 'post',
        url: `${API_URL}/movies/${movieId}/wish/`,
        headers: {Authorization: `Token ${localStorage.getItem('token')}`}
      })
      .then((response)=>{
        context.commit('WISH_MOVIE', response.data)
      })
      .catch((err)=>{
        console.log(err)
      })
    }
    

  },
  modules: {
  }
})
