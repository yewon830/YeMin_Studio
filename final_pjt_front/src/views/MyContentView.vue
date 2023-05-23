<template>
    <div>
      <h1 >내가 좋아요 한 컨텐츠</h1>
      <div class="container d-flex">
        <div class="row">
          <div class="col-md-12">
            <div id="Carousel" class="carousel slide">
              <div class="carousel-inner">
                <div v-for="(group, index) in groupedLikeMovieList" :key="index" :class="['carousel-item', index === 0 ? 'active' : '']">
                  <div class="row">
                    <div v-for="movie in group" :key="movie.id" class="col-md-2">
                      <a href="#" class="thumbnail">
                        <img class="m-4" :src="`http://image.tmdb.org/t/p/w200${movie.poster_path}`" alt="Image">
                      </a>
                    </div>
                  </div>
                </div>
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#Carousel" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#Carousel" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
          </div>
        </div>
      </div>
      <h1>나의 위시리스트</h1>
      <div class="container d-flex">
        <div class="row">
          <div class="col-md-12">
            <div id="Carousel2" class="carousel slide">
              <div class="carousel-inner">
                <div v-for="(group, index) in groupedWishMovieList" :key="index" :class="['carousel-item', index === 0 ? 'active' : '']">
                  <div class="row">
                    <div v-for="movie in group" :key="movie.id" class="col-md-2">
                      <a href="#" class="thumbnail">
                        <img class="m-4" :src="`http://image.tmdb.org/t/p/w200${movie.poster_path}`" alt="Image">
                      </a>
                    </div>
                  </div>
                </div>
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#Carousel2" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#Carousel2" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    name: 'MyContent',
    data() {
      return {
        LikeMovieList: null,
        WishMovieList: null,
      }
    },
    computed: {
      groupedLikeMovieList() {
        if (!this.LikeMovieList) return []
  
        const groups = []
        const groupSize = 5
        const totalMovies = this.LikeMovieList.length
        for (let i = 0; i < totalMovies; i += groupSize) {
          groups.push(this.LikeMovieList.slice(i, i + groupSize))
        }
        return groups
      },
      groupedWishMovieList(){
        if(!this.WishMovieList) return []
        const groups = []
        const totalMovies = this.WishMovieList.length
        for (let i=0; i<totalMovies; i+=5){
            groups.push(this.WishMovieList.slice(i,i+5))
        }
        return groups
      }
    },
    created() {
      this.getUserMovieList()
    },
    methods: {
      getUserMovieList() {
        axios({
          url: 'https://api.themoviedb.org/3/movie/top_rated?api_key=cdb84e32fe9892b6b1fad1b2dceb89d0&language=ko-KR&page=1',
        })
          .then((response) => {
            console.log(response)
            this.LikeMovieList = response.data.results
            this.WishMovieList = response.data.results
          })
          .catch((err) => {
            console.log(err)
          })
      },
    },
  }
  </script>
  
  <style>
  
  </style>
  