import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
// import router from '../router'
Vue.use(Vuex)


// const API_URL = 'http://127.0.0.1:8000'
export default new Vuex.Store({
  state: {
    movies : [],
    token : null,
  },
  getters: {
  },
  mutations: {
    GET_MOVIES(state, movies){
      state.movies = movies
    },
    // SAVE_TOKEN(state, token){
    //   state.token = token
    //   router.push({name:'MovieView'})
    // }
  },
  actions: {
    getMovies(context){
      axios({
        method: 'get',
        // url: `${API_URL}/movies/`,
        url : 'https://api.themoviedb.org/3/movie/top_rated?api_key=cdb84e32fe9892b6b1fad1b2dceb89d0&language=ko-KR&page=1'
      })
      .then((response)=>{
        context.commit('GET_MOVIES', response.data.results)
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    // signUp(context,payload){
    //   const username = payload.username
    //   const email = payload.email
    //   const password1 = payload.password1
    //   const password2 = payload.password2
    //   axios({
    //     method: 'post',
    //     url : `${API_URL}/accounts/signup/`,
    //     data : {
    //       username, email, password1,password2
    //     }
    //   })
    //   .then((response)=>{
    //     context.commit('SAVE_TOKEN', response.data.key)
    //   })
    //   .catch((err)=>{
    //     console.log(err)
    //   })
      
    // },
    // login(context,payload){
    //   const email = payload.email
    //   const password = payload.email

    //   axios({
    //     method: 'post',
    //     url: `${API_URL}/accounts/login/`,
    //     data : {
    //       email,password
    //     }
    //   })
    //   .then((response)=>{
    //     context.commit('SAVE_TOKEN',response.data.key)
    //   })
    //   .catch((err)=>{
    //     console.log(err)
    //   })
    // }
    

  },
  modules: {
  }
})
