<template>
  <div>
    <h1>댓글</h1>
    <CommentForm :articleId="articleId"/>
    <CommentList :articleId="articleId"/>
  </div>
</template>

<script>
import CommentList from '@/components/CommentList'
import CommentForm from '@/components/CommentForm'
export default {
    name:'CommentView',
    props:{
      articleId : Number
    },
    components: {
        CommentList,
        CommentForm
    }

}
</script>

<style>

</style>