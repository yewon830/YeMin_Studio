<template>
  <div>
    <form @submit.prevent="commentCreate">
        <input class="comment-input" type="text" v-model="content">
        <button class="btn btn-primary">작성</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name:'CommentForm',
    props:{
      articleId : Number
    },
    data(){
        return{
            content: null,
        }
    },
    methods: {
        commentCreate(){
            const content = this.content
            axios({
                method: 'post',
                url: `http://127.0.0.1:8000/articles/${this.articleId}/create/comments/`,
                data: {content},
                headers: {
                    Authorization: `Token ${this.$store.state.token}`
                },
            })
            .then(()=>{
                this.$store.dispatch('getCommentList',this.articleId)
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

.comment-input{
    border: 1px solid lightgrey;
    width: 820px;
    height: 102px;
    margin: 30px;
    border-radius: 2px;

}

</style>