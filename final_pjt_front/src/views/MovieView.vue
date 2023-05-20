<template>
  <div>
    <h1>MovieView</h1>
    <MovieItem v-for="movie in movies" :key="movie" :movie="movie" />
    <div class="d-flex">
      <a href="http://localhost:8080/movies/?page=1">처음으로</a>
      <button @click="prevPage">이전</button>
      <div v-for="i in displayPerPage" :key="i">
        <a :href="`http://localhost:8080/movies/?page=${i}`">{{ i }}</a>
      </div>
      <button @click="nextPage">다음</button>
      <a :href="`http://localhost:8080/movies/?page=${totalPage}`">마지막으로</a>
    </div>
  </div>
</template>

<script>
import MovieItem from '../components/MovieItem.vue'
import axios from 'axios'

export default {
  name: 'MovieView',
  components: {
    MovieItem,
  },
  data() {
    return {
      movies: null,
      totalPage : 34,
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
        url: `http://127.0.0.1:8000/movies/?page=${this.currentPage}/`,
      })
        .then((response) => {
          console.log(response)
          this.movies = response.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    nextPage() {
      if (this.startPage + 10 <= this.totalPage) {
        const nextPage = this.startPage + 10
        window.location.href = `http://localhost:8080/movies/?page=${nextPage}`
      }
    },
    prevPage() {
      if (this.startPage > 10) {
        const prevPage = this.startPage - 10
        window.location.href = `http://localhost:8080/movies/?page=${prevPage}`
      }
    },
  },
}
</script>

<style>
</style>
