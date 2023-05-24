<template>
  <div>
    <div v-for="review in reviews" :key="review.id" >
        <span>{{review.content }}|</span>
        <span>작성자{{ review.username }}</span>
        <div v-if="currentUsername === review.username">
            <button @click="deleteReview(review.id)">삭제</button>
            <button @click="addList(review.id)">수정</button>
            <div v-if="isBtnClicked(review.id)">
                <form @submit.prevent="updateReview(review.id)">
                    <input type="text" v-model="content" style="width: 500px; height: 80px;">
                    <button>작성</button>
                </form>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'ReviewList',
    props:{
        movieId: Number
    },
    data(){
        return{
            clickedBtn : null,
            content : null,
        }
    },
    computed:{
        reviews(){
            return this.$store.getters.computedReviewList
        },
        currentUsername(){
            return this.$store.state.username
        },
    },
    created(){
        this.getMovieReviews(this.movieId)
    },
    methods:{
        getMovieReviews(){
            const movieId = movieId
            this.$store.dispatch('getReviewList', movieId)
        },
        deleteReview(reviewId){
            this.$store.dispatch('deleteReview', reviewId)
        },
        isBtnClicked(reviewId){
            return this.clickedBtn === reviewId
        },
        addList(reviewId){
            if(this.clickedBtn){
                this.clickedBtn = null
            } else{
                this.clickedBtn = reviewId
            }
            axios({
                url: `http://127.0.0.1:8000/movies/reviews/${reviewId}/`,
                headers: {
                    Authorization: `Token ${this.$store.state.token}`
                },
            })
            .then((response)=>{
                this.content = response.data.content
            })

        },
        updateReview(reviewId){
            const content = this.content
            axios({
                method: 'put',
                url: `http://127.0.0.1:8000/movies/reviews/${reviewId}/`,
                headers: {
                    Authorization: `Token ${this.$store.state.token}`
                },
                data: {
                    content
                }
            })
            .then(()=>{
                const movieId = movieId
                this.$store.dispatch('getReviewList', movieId)
                this.content = null
            })
            .catch((err)=>{
                console.log(err)
            })
        }

    }
}
</script>

<style>

</style>