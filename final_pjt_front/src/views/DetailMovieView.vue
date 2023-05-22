<template>
  <div class="modal-container">
    <button @click="closeModal">닫기</button>
    <MovieDetailVideo :movie="movie" />
    <div>
      <router-link :to="{ name: 'ReviewView', params: { movieId: $route.params.movieId } }">리뷰 보기</router-link>
    </div>
    <router-view />
  </div>
</template>

<script>
import axios from 'axios';
import MovieDetailVideo from '@/components/MovieDetailVideo';

export default {
  name: 'DetailMovieView',
  created() {
    this.getDetailMovie();
  },
  components: {
    MovieDetailVideo,
  },
  data() {
    return {
      movie: null,
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
      this.$emit('close');
    },
  },
};
</script>

<style>
.modal-container {
  position: fixed;
  top: 45%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 50%;
  height: 80vh;
  background-color: #fff;
  border-radius: 8px;
  padding: 20px;
  z-index: 9999;
}

.modal-container::before {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* 반투명한 효과를 위해 rgba 색상 사용 */
  z-index: 9998;
}
</style>