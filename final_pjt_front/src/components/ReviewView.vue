<template>
  <div>
    <h1>리뷰</h1>
    <ReviewForm :movieId="movieId"/>
    <ReviewList :movieId="movieId"/>
  </div>
</template>

<script>
import ReviewForm from '@/components/ReviewForm'
import ReviewList from '@/components/ReviewList'
export default {
  name: 'ReviewView',
  props: {
    movieId : Number
  },
  components: {
    ReviewForm,
    ReviewList,
  }
}
</script>

<style>

</style>