<template>
  <div>
    <h1>댓글</h1>
    <CommentForm/>
    <CommentList/>
  </div>
</template>

<script>
import CommentList from '@/components/CommentList'
import CommentForm from '@/components/CommentForm'
export default {
    name:'CommentView',
    components: {
        CommentList,
        CommentForm
    }

}
</script>

<style>

</style>