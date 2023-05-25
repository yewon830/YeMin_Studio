<template>
  <div class="modal-container" style="color: black;">
    <div >
      <div>
        <iframe width="100%" height="355" :src="'https://www.youtube.com/embed/' + movie.video_key +'?autoplay=1'" frameborder="0" allowfullscreen></iframe>
      </div>
      <div>
        <h5>{{ movie.title }}</h5>
      </div>
      <div @click="likeMovie">
        <font-awesome-icon :color="getHeartColor(movie.id)" :icon="['fas', 'heart']" size="lg" />
      </div>
      <div @click="wishMovie">
        <font-awesome-icon :color="getWishColor(movie.id)" :icon="['fasl', 'folder-open']" size="lg" />
      </div>
      <div style="font-size: 0.875rem;">
        <div style="min-height: 29.125rem; font-size: 0.875rem;">
          <p class="text-overview">{{ movie.overview }}</p>
          <input type="checkbox" class="more-btn">
        </div>
      </div>
      <div>
        <div>
          <h6>감독</h6>
          <span>{{ movie.director.name }}</span>
        </div>
      </div>
      <div>
        <h6>배우</h6>
        <div>
          <div v-for="actor in movie.actors" :key="actor.name">
            <span>{{ actor.name }}</span>
          </div>
          <div>
            <h6>개봉날짜</h6>
            <span>{{ movie.release_date }}</span>
          </div>
        </div>
      </div>
    </div>
    <div>
      <button @click="showReview" class="btn btn-primary">
        리뷰 보기
      </button>
      <div v-if="isBtnClicked">
        <ReviewView :movieId="movie.id"/>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
import ReviewView from '@/components/ReviewView'


export default {
  name: 'DetailMovieView',
  components: {

    ReviewView
  },
  computed:{
    movie(){
      return this.$store.getters.computedDetailMovie
    },
    likeMovieData(){
      return this.$store.getters.computedLikeMovie
    },
    wishMovieData(){
      return this.$store.getters.computedWishMovie
    }
  },
  data() {
    return {
      // movie: null,
      showModal: true,
      isBtnClicked : false,
      isHeartClicked: false,
      isWishClicked: false,
      heartColor: 'black',
      wishColor: 'black'
    };
  },

  methods: {
    likeMovie(){
    this.$store.dispatch('likeMovie', this.movie.id)
    this.getHeartColor()
    this.$store.dispatch('myContentList')
    },
    wishMovie(){
        this.$store.dispatch('wishMovie', this.movie.id)
        this.getWishColor()
        this.$store.dispatch('myContentList')
    },
    getHeartColor() {
      // console.log(this.likeMovieData)
      if(this.likeMovieData){
        const isLike = this.likeMovieData.includes(this.movie.id)
        return isLike ? '#0d6efd' : 'black'
      }else{
        return 'black'
      }
      
    },
    getWishColor(){
      if(this.wishMovieData){
        const isWished = this.wishMovieData.includes(this.movie.id)
        return isWished ? '#0d6efd' : 'black'
      }else{
        return 'black'
      }
      
    },
    showReview(){
      this.isBtnClicked = !this.isBtnClicked
    }

  },
};
</script>

<style>
  .modal,.overlay{
      width: 100%;
      height: 100%;
      position: fixed;
  }
  .movie-info{
      padding: 40px 40px 40px 40px;
  }
  .text-overview{
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
      margin-bottom: 0px;
  }
  .more-btn{
      appearance: none;
      border: none;
      padding: 0.5em;
      cursor: pointer;
  }
  .more-btn::before{
      content: '더보기';
      color: #4590e3;
  }
  .more-btn:checked::before{
      content: '닫기';
      color: #4590e3;
  }
  .text-overview:has(+ .more-btn:checked){
      -webkit-line-clamp:unset;
  }
  h6{
      margin-right:10px;
  }
  aside{
      font-size: 0.875rem;
  }
  aside span{
      color: #d4d7db;
  }
</style>