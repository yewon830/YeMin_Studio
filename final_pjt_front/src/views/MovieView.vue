<template>
  <div >
    <h1 class="text-start">영화 목록</h1>
    <div class="d-flex container-fluid row row-cols-1 row-cols-md-6 g-4" >
      <MovieItem v-for="movie in movies" :key="movie.title" :movie="movie" @openModal="openModal" />
    </div>
    
    <div class="d-flex justify-content-center">
      <a class="page-button" href="http://localhost:8080/movies/1" >처음으로</a>
      <button class="page-button" @click="prevPage">이전</button>
      <div v-for="i in displayPerPage" :key="i">
        <a class="page-button" :href="`http://localhost:8080/movies/${i}`">{{ i }}</a>
      </div>
      <button class="page-button" @click="nextPage">다음</button>
      <a class="page-button" :href="`http://localhost:8080/movies/${totalPage}`">마지막으로</a>
    </div>
  </div>
</template>

<script>
// import DetailMovieView from '@/views/DetailMovieView'
import MovieItem from '../components/MovieItem.vue'
import axios from 'axios'

export default {
  name: 'MovieView',
  components: {
    MovieItem,
    // DetailMovieView
  },
  data() {
    return {
      movies: null,
      totalPage : 34,
      ShowModal : false,
      selectedMovie : null
    }
  },
  computed: {
    displayPerPage() {
      if (this.startPage + 9 > this.totalPage){
        return Array.from({ length: 4 }, (_, index) => this.startPage + index)
      } else{
        return Array.from({ length: 10 }, (_, index) => this.startPage + index)
      }
      
    },
    currentPage() {
      return parseInt(this.$route.params.page) || 1
    },
    startPage() {
      return Math.floor((this.currentPage - 1) / 10) * 10 + 1
    },
    
  },
  created() {
    this.getPerPageMovies()
  },
  methods: {
    getPerPageMovies() {
      axios({
        url: `http://127.0.0.1:8000/movies/${this.currentPage}/`,
      })
        .then((response) => {
          this.movies = response.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    nextPage() {
      if (this.startPage + 10 <= this.totalPage) {
        const nextPage = this.startPage + 10
        window.location.href = `http://localhost:8080/movies/${nextPage}`
      }
    },
    prevPage() {
      if (this.startPage > 10) {
        const prevPage = this.startPage - 10
        window.location.href = `http://localhost:8080/movies/${prevPage}`
      }
    },
    openModal(movieId){
      // console.log(movieId)
      this.ShowModal = true
      this.selectedMovieId = movieId

    },
    closeModal(){
      this.ShowModal = false
      this.selectedMovie = null
    }
  },
}
</script>

<style>
.text-start {
  text-align: start;
  margin-left: 30px;
  margin-top: 10px;
}
.page-button{
  padding-left: 2px;
  padding-right: 2px;
}

</style>
