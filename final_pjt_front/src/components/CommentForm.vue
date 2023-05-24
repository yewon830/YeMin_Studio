<template>
  <div>
    <form @submit.prevent="commentCreate">
        <input type="text" style="width: 500px; height: 80px;" v-model="content">
        <button>작성</button>


    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name:'CommentForm',
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
                url: `http://127.0.0.1:8000/articles/${this.$route.params.articleId}/comments/`,
                data: {content},
                headers: {
                    Authorization: `Token ${this.$store.state.token}`
                },
            })
            .then(()=>{
                this.$store.dispatch('getCommentList')
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

</style>