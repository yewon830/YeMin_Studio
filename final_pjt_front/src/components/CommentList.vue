<template>
  <div>
    <div v-for="comment in comments" :key="comment.id">
        <span>{{comment.content}}</span>
        <span>작성자 : {{comment.username}}</span>
        <div v-if="currentUsername === comment.username">
            <button @click="deleteComment(comment.id)">삭제</button>
        </div>
        
    </div>
  </div>
</template>

<script>

export default {
    name:'CommentList',
    computed: {
        comments(){
            return this.$store.getters.computedCommentList
        },
        currentUsername(){
            return this.$store.state.username
        }
    },
    created(){
        this.getCommentList()
    },
    methods: {
        getCommentList(){
            this.$store.dispatch('getCommentList')
        },
        deleteComment(commentId){
            this.$store.dispatch('deleteComment',commentId)
        }
    }
}
</script>

<style>

</style>