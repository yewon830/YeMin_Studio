<template>
  <div>
    <h1>{{article?.title}}</h1>
    <span>{{article?.user.username}}</span>
    <p>작성 시간 : {{article?.created_at}}</p>
    <p>수정 시간 : {{article?.updated_at}}</p>
    <p>{{article?.content}}</p>

    <a :href="`http://localhost:8080/articles/${this.$route.params.articleId}/update`">수정하기</a>
    <button @click="deleteArticle">삭제하기</button>


    <Comment/>

  </div>
</template>

<script>
import Comment from '@/components/Comment'
import axios from 'axios'
export default {
    name: 'ArticleDetailView',
    components: {
        Comment
    },
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
    created(){
        this.getArticleDetail()
    },
    methods:{
        getArticleDetail(){
            axios({
                url: `http://127.0.0.1:8000/articles/${this.$route.params.articleId}/`,
                headers: {
                Authorization: `Token ${this.$store.state.token}`
                },
            })
            .then((response)=>{
                this.article = response.data
            })
            .catch((err)=>{
                console.log(err)
            })
        },
        deleteArticle(){
            this.$store.dispatch('deleteArticle',this.$route.params.articleId)
        }
    }
}
</script>


<style>

</style>