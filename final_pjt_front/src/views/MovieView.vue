<template>
  <div >
    <h1 class="text-start">영화 목록</h1>
    <div class="d-flex justify-content-center mt-4">
      <button class="sort-button" :class="{ active: sortOption === 'popularity' }" @click="changeSortOption('popularity')">인기순</button>
      <button class="sort-button" :class="{ active: sortOption === 'vote_average' }" @click="changeSortOption('vote_average')">평점순</button>
      <button class="sort-button" :class="{ active: sortOption === 'title' }" @click="changeSortOption('title')">가나다순</button>
    </div>
    <div class="d-flex container-fluid row row-cols-1 row-cols-md-6 g-4" >
      <MovieItem v-for="movie in movies" :key="movie.title" :movie="movie" @openModal="openModal" />
    </div>
    
    <div class="d-flex justify-content-center">
      <a class="page-button" :href="getPageUrl(1)+sortOption">처음으로</a>
      <button class="page-button" @click="prevPage">이전</button>
      <div v-for="i in displayPerPage" :key="i">
        <a class="page-button" :class="{ active: i === currentPage }" :href="`${getPageUrl(i)}${sortOption}`">{{ i }}</a>
      </div>
      <button class="page-button" @click="nextPage">다음</button>
      <a class="page-button" :href="getPageUrl(totalPage)+sortOption">마지막으로</a>
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
      totalPage: 34,
      showModal: false,
      selectedMovie: null,
      sortOption: this.$route.query.sort || 'movie_id' // 기본 정렬 옵션 설정
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
  watch: {
    currentPage: {
      handler() {
        this.getPerPageMovies();
      },
      immediate: true // 초기 로드시에도 호출되도록 immediate 옵션을 추가합니다.
    }
  },
  methods: {
    getPerPageMovies() {
      axios({
        url: `http://127.0.0.1:8000/movies/${this.currentPage}/?sort=${this.sortOption}`,
      })
        .then((response) => {
          this.movies = response.data.movies
          this.sortOption = response.data.sort_option // 응답에서 정렬 기준을 받아옴
        })
        .catch((err) => {
          console.log(err)
        })
    },
    prevPage() {
      if (this.startPage > 10) {
        const prevPage = this.startPage - 10;
        const query = `sort=${this.sortOption}`;
        const url = `/movies/${prevPage}?${query}`;
        window.location.href = url;
      }
    },
    nextPage() {
      if (this.startPage + 10 <= this.totalPage) {
        const nextPage = this.startPage + 10;
        const query = `sort=${this.sortOption}`;
        const url = `/movies/${nextPage}?${query}`;
        window.location.href = url;
      }
    },
    openModal(movieId){
      // console.log(movieId)
      this.ShowModal = true
      this.selectedMovieId = movieId

    },
    closeModal(){
      this.ShowModal = false
    },
    changeSortOption(option) {
    if (this.sortOption !== option) {
      this.sortOption = option
      this.getPerPageMovies()

      const currentPage = this.currentPage
      const query = `sort=${this.sortOption}`

      this.$router.push(`/movies/${currentPage}?${query}`)
      }
    },
    getPageUrl(page) {
      return `http://localhost:8080/movies/${page}?sort=`
    },
    // 정렬 옵션에 따라서...다른 url 을 생성하기 
    // 정렬 옵션을 선택하면 반복문으로 만들어진 html 요소의 href 속성을 바꿀 수 있니??
    //
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
