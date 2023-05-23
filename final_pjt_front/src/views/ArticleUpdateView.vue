<template>
  <div>
    <h1>게시글 수정</h1>
    <form @submit="updateArticleDetail">
        <input type="text" v-model="title">
        <textarea cols="30" rows="10" v-model="content"></textarea>
        <button>수정</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name:'ArticleUpdate',
    data(){
        return{
            title : null,
            content: null
        }
    },
    created(){
        this.getArticleDetail()
    },
    methods: {
        getArticleDetail(){
            axios({
                url: `http://127.0.0.1:8000/articles/${this.$route.params.articleId}/`,
                headers: {
                Authorization: `Token ${this.$store.state.token}`
                },
       
            })
            .then((response)=>{
                this.title = response.data.title
                this.content = response.data.content
            })
            .catch((err)=>{
                console.log(err)
            })

        },
        updateArticleDetail(){
            const title = this.title
            const content = this.content
            if(!this.title){
                alert('제목을 입력해주세요')
                return
            }  else if(!this.content){
                alert('내용을 입력해주세요')
                return
            }
            axios({
                method: 'put',
                url: `http://127.0.0.1:8000/articles/${this.$route.params.articleId}/`,
                data: {
                    title,content
                },
                headers: {
                Authorization: `Token ${this.$store.state.token}`
                },
            })
            .catch((err)=>{
                console.log(err)
            })
            this.$router.push({name:'ArticleDetailView', params:{articleId: this.$route.params.articleId}})
        }
    }
}
</script>

<style>

</style>