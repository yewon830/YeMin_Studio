<template>
  <div>
    <form @submit.prevent="onSubmit">
        <input type="text" placeholder="리뷰를 작성해주세요" v-model="content">
            <div class="star-rating">
            <input v-model="rank" type="radio" id="5-stars" name="rating" value="5" />
            <label  for="5-stars" class="star">&#9733;</label>
            <input v-model="rank" type="radio" id="4-stars" name="rating" value="4" />
            <label for="4-stars" class="star">&#9733;</label>
            <input v-model="rank" type="radio" id="3-stars" name="rating" value="3" />
            <label for="3-stars" class="star">&#9733;</label>
            <input v-model="rank" type="radio" id="2-stars" name="rating" value="2" />
            <label for="2-stars" class="star">&#9733;</label>
            <input v-model="rank" type="radio" id="1-star" name="rating" value="1" />
            <label for="1-star" class="star">&#9733;</label>
            </div>
        <button>작성</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {

    name: 'ReviewForm',
    props:{
        movieId: Number
    },
    data(){
        return{
            content: null,
            rank: null
        }
    },
    methods: {
        onSubmit(){
            const content = this.content
            const rank = this.rank
            const movieId = this.movieId
            console.log(this.movieId)
            if (!content || !movieId) {
                alert('리뷰를 작성해주세요')
                return
            }
            axios({
                method: 'post',
                url: `http://127.0.0.1:8000/movies/reviews/create/${movieId}/`,
                headers: {
                    Authorization: `Token ${this.$store.state.token}`
                },
                data: {content,rank, movie_id: movieId}
            })
            .then(()=>{
                this.$store.dispatch('getReviewList', movieId)
                this.content = null
                this.rank = null
            })
            .catch((err)=>{
                console.log(err)
            })
        }
    }
}
</script>

<style>
.star-rating {
  border:solid 1px #ccc;
  display:flex;
  flex-direction: row-reverse;
  font-size:1.5em;
  justify-content:space-around;
  padding:0 .2em;
  text-align:center;
  width:5em;
}

.star-rating input {
  display:none;
}

.star-rating label {
  color:#ccc;
  cursor:pointer;
}

.star-rating :checked ~ label {
  color:#f90;
}

.star-rating label:hover,
.star-rating label:hover ~ label {
  color:#fc0;
}


</style>