<template>
  <div>
    <h1>게시글 수정</h1>
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
            if(!this.title){
                alert('제목을 입력해주세요')
                return
            }  else if(!this.content){
                alert('내용을 입력해주세요')
                return
            }
            axios({
                method: 'put',
                url: `http://127.0.0.1:8000/articles/update/${this.$route.params.articleId}/`,
                data: {
                    title,content
                },
                headers: {
                Authorization: `Token ${this.$store.state.token}`
                },
            })
            .then(()=>{
                this.$router.push({name:'ArticleDetailView', params:{articleId: this.$route.params.articleId}})
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