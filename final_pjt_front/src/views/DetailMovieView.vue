<template>
  <div class="modal-container">
    <div class="overlay" v-if="showModal" @click.self="closeModal"></div>
    <div class="modal-container" v-if="showModal">
      <button class="modal-close-button" @click="closeModal">닫기</button>
      <MovieDetailVideo :movie="movie" />
    </div>
    <button @click="showReview">리뷰 보기</button>
    <div v-if="isBtnClicked">
      <!-- 리뷰 보여줘야 함 -->
      <ReviewView :movie-id="movie.id"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ReviewView from '@/components/ReviewView'
import MovieDetailVideo from '@/components/MovieDetailVideo';

export default {
  name: 'DetailMovieView',
  created() {
    this.getDetailMovie()
    this.$emit('open-modal', this.$route.params.movieId)
  },
  components: {
    MovieDetailVideo,
    ReviewView
  },
  data() {
    return {
      movie: null,
      showModal: true,
      isBtnClicked : false,
    };
  },
  methods: {
    getDetailMovie() {
      axios({
        url: `http://127.0.0.1:8000/movies/d=${this.$route.params.movieId}/`,
      })
        .then((response) => {
          console.log(response.data);
          this.movie = response.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    closeModal() {
      this.showModal = false
      this.$router.go(-1) // 이전 페이지로 이동
    },
    showReview(){
      this.isBtnClicked = !this.isBtnClicked
    }
  },
};
</script>

<style>
body.modal-open {
  overflow: hidden;
}
.modal-container {
  position: fixed;
  top: 45%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 50%;
  height: 80vh;
  background-color: rgba(6, 5, 58, 0.932);
  color: white;
  border-radius: 8px;
  padding: 20px;
  z-index: 9999;
}

.modal-close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  padding: 5px 10px;
  background-color: #ccc;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.modal-close-button:hover {
  background-color: #aaa;
}

.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.3);
  z-index: 9998;
}
</style>