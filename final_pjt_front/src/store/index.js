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
    likeMovie: [],
    wishMovie:[],
    username: null,
    userProfile : {},
    currentUser: {},
    personalMovieList : {},
    //
    ArticleList : [],

  },
  getters: {
    isLogin(state){
      return state.token ? true : false
    },
    authHeader(state){
      return ({ Authorization: `Token ${state.token}` })
    }
  },
  mutations: {
    SAVE_TOKEN(state, token){
      state.token = token
      router.push({name:'MovieView'})
    },
    LIKE_MOVIE(state, movie){
      state.likeMovie = movie
    },
    WISH_MOVIE(state,movie){
      state.wishMovie = movie
    },
    SAVE_USERNAME(state,username){
      state.username = username
    },
    GET_USER_PROFILE(state, userInfo){
      state.userProfile = userInfo
    },
    REMOVE_TOKEN(state){
      state.token = null
      state.username = null
    },
    UPDATE_PROFILE(state,userInfo){
      state.currentUser = userInfo
    },
    GET_USER_MOVIE_LIST(state,movieList){
      state.personalMovieList = movieList
    },
    GET_ARTICLELIST(state,articleList){
      state.articleList = articleList
    }

  },
  actions: {

    signUp(context, payload) {
      const username = payload.username
      const email = payload.email
      const password1 = payload.password1
      const password2 = payload.password2
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, email, password1, password2
        }
      })
        .then((response) => {
          const { success, access } = response.data // 토큰 정보 받아옴
          context.commit('SAVE_TOKEN', access) // 토큰 저장
          console.log(success)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    login(context, payload) {
      const username = payload.username
      const password = payload.password
    
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then((response) => {
          // console.log(response)
          const data1 = JSON.parse(response.config.data)
          // const { success, access } = response.data // 토큰 정보 받아옴
          context.commit('SAVE_TOKEN', response.data.key) // 토큰 저장
          context.commit('SAVE_USERNAME', data1.username)
          // console.log(response.data.key)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    updateProfile(context,payload){
      const username = payload.username
      const email = payload.email
      const password1 = payload.password1
      const password2 = payload.password2
      axios({
        method: 'put',
        url: `${API_URL}/accounts/profile/update/`,
        data : {
          username,email,password1,password2
        },
        headers : context.getters.authHeader
      })
      .then((response)=>{
        context.commit('UPDATE_PROFILE',response.data)

      })
      .catch((err)=>{
        console.log(err)
      })
    },
    likeMovie(context,movieId){
      console.log(context.getters.authHeader)
      axios({
        method:'post',
        url: `${API_URL}/movies/${movieId}/likes/`,
        headers:{
          Authorization : `Token ${this.state.token}`
        }
      })
      .then((response)=>{
        context.commit('LIKE_MOVIE', response.data)
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    wishMovie(context,movieId){
      console.log(context.getters.authHeader)
      axios({
        method: 'post',
        url: `${API_URL}/movies/${movieId}/wish/`,
        headers: {
          Authorization : `Token ${this.state.token}`
        }
      })
      .then((response)=>{
        context.commit('WISH_MOVIE', response.data)
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    getUserProfile(context){
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/${context.state.username}/`,
        headers : context.getters.authHeader
      })
      .then((response)=>{
        context.commit('GET_USER_PROFILE', response.data)
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    logout(context) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
        headers : {
          Authorization : `Token ${this.state.token}`
        } 
      })
      .then(() => {
        context.commit('REMOVE_TOKEN')
        localStorage.removeItem('vuex')
        router.push({ name: 'HomeView' })
      })
      .catch((error) => {
        console.log(error)
      })
    },
    getUserMovieList(context){
      axios({
        url: `${API_URL}/accounts/movie_list/${this.state.username}/`,
        headers : {
          Authorization : `Token ${this.state.token}`
        } 
      })
      .then((response)=>{
        context.commit('GET_USER_MOVIE_LIST', response.data)
      })
      .catch((err)=>{
        console.log(err)
      })
    },

    ////////////////아티클
    getArticleList(context){
      axios({
        url: `${API_URL}/articles/`,
        headers : {
          Authorization : `Token ${this.state.token}`
        }
      })
      .then((response)=>{
        context.commit('GET_ARTICLELIST',response.data)
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    deleteArticle(context,payload){
      axios({
        method: 'delete',
        url: `${API_URL}/articles/${payload}`,
        headers : {
          Authorization : `Token ${this.state.token}`
        }
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  },
  modules: {
  }
})
