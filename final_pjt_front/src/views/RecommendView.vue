<template>
  <div>
    <h1>추천 창</h1>
    <button @click="getRecommendMovieList">새로 추천받기</button>

    <div class="movie-image-container container">
      <p >
      백만명의 사람들이 내 영화를 보았다면 나는 그들이 백만개의 다른 영화를 보았으면 한다.
        - 쿠엔틴 타란티노 -
      </p>
  <div class="carousel2">

    <div class="carousel__face thumbnail movie-item" data-bs-target="#exampleModal" data-bs-toggle="modal" @click="openModal(recommendMovieList[0].id)">
      <span>영화란</span>
      <img class="movie-image" :src="`http://image.tmdb.org/t/p/w200${recommendMovieList[0].poster_path}`" alt="">
      <div class="movie-info d-flex flex-column">
        <span class="hover-title recommend-span">{{ recommendMovieList[0].title }}</span>
        <span class="recommend-span"> ★{{ recommendMovieList[0].vote_average  }}</span>
      </div>
      
      </div>
    <div class="carousel__face thumbnail movie-item" data-bs-target="#exampleModal" data-bs-toggle="modal" @click="openModal(recommendMovieList[1].id)">
      <span>지루한</span>
      <img class="movie-image" :src="`http://image.tmdb.org/t/p/w200${recommendMovieList[1].poster_path}`" alt="">
      <div class="movie-info d-flex flex-column">
        <span class="hover-title recommend-span">{{ recommendMovieList[1].title }}</span>
        <span class="recommend-span">★{{ recommendMovieList[1].vote_average  }}</span>
      </div>
      
      </div>
    <div class="carousel__face thumbnail movie-item" data-bs-target="#exampleModal" data-bs-toggle="modal" @click="openModal(recommendMovieList[2].id)">
      <span>부분이</span>
      <img class="movie-image" :src="`http://image.tmdb.org/t/p/w200${recommendMovieList[2].poster_path}`" alt="">
      <div class="movie-info d-flex flex-column">
        <span class="hover-title recommend-span">{{ recommendMovieList[2].title }}</span>
        <span class="recommend-span">★{{ recommendMovieList[2].vote_average  }}</span>
      </div>
      
      </div>
    <div class="carousel__face thumbnail movie-item" data-bs-target="#exampleModal" data-bs-toggle="modal" @click="openModal(recommendMovieList[3].id)">
      <span>커트된</span>
      <img class="movie-image" :src="`http://image.tmdb.org/t/p/w200${recommendMovieList[3].poster_path}`" alt="">
      <div class="movie-info d-flex flex-column">
        <span class="hover-title recommend-span">{{ recommendMovieList[3].title }}</span>
        <span class="recommend-span">★{{ recommendMovieList[3].vote_average  }}</span>
      </div>
      
      </div>
    <div class="carousel__face thumbnail movie-item" data-bs-target="#exampleModal" data-bs-toggle="modal" @click="openModal(recommendMovieList[4].id)">
      <span>인생이다</span>
      <img class="movie-image" :src="`http://image.tmdb.org/t/p/w200${recommendMovieList[4].poster_path}`" alt="">
      <div class="movie-info d-flex flex-column">
        <span class="hover-title recommend-span">{{ recommendMovieList[4].title }}</span>
        <span class="recommend-span">★{{ recommendMovieList[4].vote_average  }}</span>
      </div>
      
   </div>
  </div>
</div>


<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-xl">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div>
            <DetailMovieView />
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary">Save changes</button>
        </div>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import DetailMovieView from '@/views/DetailMovieView.vue'
import axios from 'axios'
export default {
    name: 'RecommendView',
    components:{
      DetailMovieView
    },
    data(){
      return{
        recommendMovieList : []
      }
    },
    created(){
      this.getRecommendMovieList()
    },
    methods:{
      getRecommendMovieList(){
        axios({
          url:`http://127.0.0.1:8000/accounts/commend/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          },
        })
        .then((response)=>{
          this.recommendMovieList = response.data.movies
    
        })
        .catch((err)=>{
          console.log(err)
        })
      },
      openModal(movieId){
        this.$store.dispatch('getDetailMovie',movieId)
      }
    },
}
</script>

<style>
.container {
  position: relative;
  width: 200px;
  margin: 100px auto 0 auto;
  perspective: 1000px;
}

.carousel2 {
  position: absolute;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d; 
  animation: rotate360 40s infinite forwards linear;
}
.carousel__face { 
  position: absolute;
  width: 100%;
  height: 187px;
  top: 20px;
  left: 10px;
  right: 10px;
  /* background-size: cover; */
  box-shadow:inset 0 0 0 2000px rgba(0,0,0,0.5);
  display: flex;
}

.recommend-span {
  margin: auto;
  font-size: 1rem;
}


.carousel__face:nth-child(1) {
  
  transform: rotateY( 0deg) translateZ(430px); }
.carousel__face:nth-child(2) { 
  
    transform: rotateY( 72deg) translateZ(430px); }
.carousel__face:nth-child(3) {
  
  transform: rotateY( 144deg) translateZ(430px); }
.carousel__face:nth-child(4) {
  
  transform: rotateY(216deg) translateZ(430px); }
.carousel__face:nth-child(5) { 
  
 transform: rotateY(288deg) translateZ(430px); }

@keyframes rotate360 {
  from {
    transform: rotateY(0deg);
  }
  to {
    transform: rotateY(-360deg);
  }
}
</style>