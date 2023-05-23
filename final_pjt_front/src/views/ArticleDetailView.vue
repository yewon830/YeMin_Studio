<template>
  <div>
    <h1>{{article?.title}}</h1>
    <p>작성 시간 : {{article?.created_at}}</p>
    <p>수정 시간 : {{article?.updated_at}}</p>
    <p>{{article?.content}}</p>

    <button @click="deleteArticle">삭제하기</button>


  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'ArticleDetailView',
    data(){
        return{
            article: null
        }
    },
    computed:{
        username(){
            return this.$store.state.username
        }

    },
    methods:{
        getArticleDetail(){
            axios({
                url: `http://127.0.0.1:8000/articles/${this.$route.params.articleId}/`
            })
            .then((response)=>{
                this.article = response.data
            })
            .catch((err)=>{
                console.log(err)
            })
        },
        deleteArticle(){
            this.$store.dispatch('deleteArticle',this.$store.params.articleId)
            this.$router.push({name:'ArticleView'})
        }
    }
}
</script>


<style>

</style>