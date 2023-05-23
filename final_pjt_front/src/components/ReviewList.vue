<template>
  <div>
    <ReviewListItem v-for="review in reviewList" :key="review.id" :review="review"/>
  </div>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem'
import axios from 'axios'
export default {
    name: 'ReviewList',
    components: {
        ReviewListItem
    },
    props: {
        movieId: Number
    },
    data(){
        return {
            reviewList : []
        }
    },
    created(){
        this.getMovieReviews()
    },
    methods:{
        getMovieReviews(){
            axios({
                url: `http://127.0.0.1:8000/movies/reviews/${this.movieId}/`,
                headers: {
                    Authorization: `Token ${this.$store.state.token}`
                },
            })
            .then((response)=>{
                this.reviewList = response.data
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