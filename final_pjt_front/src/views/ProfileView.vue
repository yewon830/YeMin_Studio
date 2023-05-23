<template>
  <div>
    <h1>{{userProfile.username}}의 프로필</h1>
    <p>{{userProfile.profile_image}}</p>
    <button class="btn "></button>
    <p>팔로잉 : {{userProfile.following_count}}</p>
    <p>팔로워 : {{userProfile.followers_count}}</p>
    <h1>내가 쓴 리뷰</h1>
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