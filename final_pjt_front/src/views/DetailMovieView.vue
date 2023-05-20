<template>
  <div>
    <MovieDetailVideo :movie="movie"/>
    <div>
      <router-link :to="{name:'ReviewView', params:{movieId:this.$route.params.movieId}}">리뷰 보기</router-link>
    </div>    
    <router-view/>
  </div>
</template>

<script>
import axios from 'axios'
import MovieDetailVideo from '@/components/MovieDetailVideo'
export default {
  name: 'DetailMovieView',
  created(){
    this.getDetailMovie()
  },
  components: {
    MovieDetailVideo,
  },
  data(){
    return{
      movie : null
    }
  },
  methods: {
    getDetailMovie(){
      axios({
        url : `http://127.0.0.1:8000/movies/d=${this.$route.params.movieId}/`
      })
      .then((response)=>{
        console.log(response.data)
        this.movie = response.data
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>