<template>
  <div>
    <h1>{{userProfile.username}}의 프로필</h1>
    <p>{{userProfile.profile_image}}</p>
    <button class="btn "></button>
    <p>팔로잉 : {{userProfile.following_count}}</p>
    <p>팔로워 : {{userProfile.followers_count}}</p>
    <h1>내가 쓴 리뷰</h1>
    <div v-for="review in userProfile.reviews" :key="review.id">
        <a :href="`http://localhost:8080/movies/detail/${review.movie_id}`">
            <p>{{review.movie_id}} | </p>
            <p>{{review.content}}</p>
        </a>
    </div>
  </div>
</template>

<script>
export default {
    name: 'ProfileView',
    computed:{
        userProfile(){
            return this.$store.state.userProfile
        }
    },
    created(){
        this.getUserProfile()
    },
    methods: {
        getUserProfile(){
            this.$store.dispatch('getUserProfile')
        }
    }
}
</script>

<style>

</style>