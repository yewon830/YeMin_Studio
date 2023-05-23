<template>
  <div>
    <h1>게시글 작성하기</h1>
    <form @submit.prevent="createArticle">
        <p>제목</p>
        <input type="text" v-model.trim="title">
        <p>내용</p>
        <textarea id="article-content" cols="30" rows="10" v-model="content"></textarea>
        <input type="submit">

    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'ArticleCreateView',
    data(){
        return{
            title: null,
            content: null,
        }
    },
    methods:{
        createArticle(){
            const title = this.title
            const content = this.content
            if(!title){
                alert('제목을 입력해주세요')
                return
            }else if(!content){
                alert('내용을 입력해주세요')
                return
            }
            axios({
                method: 'post',
                url: `http://127.0.0.1:8000/articles/create/`,
                headers: {
                Authorization: `Token ${this.$store.state.token}`
                },
                data: {title,content}
            })
            .then((response)=>{
                console.log(response)
                this.$router.push({name:'ArticleView'})
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