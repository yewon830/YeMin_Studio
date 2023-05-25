<template>
  <div>
    <h1>{{userProfile.username}}의 프로필</h1>
    <p>{{userProfile.profile_image}}</p>
    <button class="btn "></button>
    <p>팔로잉 : {{userProfile.followings_count}}</p>
    <p>팔로워 : {{userProfile.followers_count}}</p>
    <h1>내가 쓴 리뷰</h1>
    <div v-for="review in userProfile.reviews" :key="review.id">
        <a data-bs-target="#exampleModal" data-bs-toggle="modal" class="thumbnail" @click="openModal(review[1])">
            <p>{{review[0]}} | </p>
            <p>{{review[1]}}</p>
        </a>
    </div>

            <!-- Modal -->
  
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
import DetailMovieView from '@/views/DetailMovieView'
export default {
    name: 'ProfileView',
    components:{
        DetailMovieView
    },
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
        },
        openModal(movieId){
            this.$store.dispatch('getDetailMovie', movieId)
        }
    }
}
</script>

<style>

</style>