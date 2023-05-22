<template>

  <div class="modal-container">
    <button @click="closeModal">닫기</button>
    <MovieDetailVideo :movie="movie"/>
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
        this.movie = response.data
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    closeModal(){
      this.$emit('close')
    }
  }
}
</script>

<style>

</style>