<template>
  <div>
    <h1 class="text-start" style="margin-top: 40px;">{{userProfile.username}}의 프로필</h1>
    <hr>
    <h3 class="text-start">내가 쓴 리뷰</h3>
    <div class="d-flex flex-column justify-content-center align-items-start m-4">
      <div style="background-color: white; width: 80%; margin: auto; min-height: 800px;">
        <div v-for="review in userProfile.reviews" :key="review.id">
        <a style="font-size: 20px;" data-bs-target="#exampleModal" data-bs-toggle="modal" class="thumbnail myreview" @click="openModal(review[1])">
            <p style="color: black;" class="text-start">{{review[0]}}</p>
            
        </a>
      </div>


      </div>


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
            this.$store.dispatch('getReviewList', movieId)
        }
    }
}
</script>

<style>
.myreview{
  text-decoration: none;
  color: white;
}
</style>