<template>
  <div>
    <div v-for="(comment) in comments" :key="comment.id">
        <span>{{comment.content}}</span>
        <span>작성자 : {{comment.username}}</span>
        <div v-if="currentUsername === comment.username">
            <button @click="deleteComment(comment.id)">삭제</button>
            <button @click="addList(comment.id)">수정</button>
            <div v-if="isBtnClicked(comment.id)">
                <form @submit.prevent="updateComment(comment.id)">
                    <input type="text" v-model="content" style="width: 500px; height: 80px;">
                    <button>작성</button>
                </form>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name:'CommentList',
    props: {
        articleId: Number
    },
    data(){
        return{
            clickedBtn: null,
            content : null,
        }
    },
    computed: {
        comments(){
            return this.$store.getters.computedCommentList
        },
        commentsCnt(){
            return this.comments.length
        },
        currentUsername(){
            return this.$store.state.username
        },
        
    },
    created(){
        this.getCommentList(this.articleId)
    },
    methods: {
        getCommentList(){
            this.$store.dispatch('getCommentList', this.articleId)
        },
        deleteComment(commentId){
            const articleId = this.articleId
            const payload = {
                commentId, articleId
            }
            this.$store.dispatch('deleteComment',payload)
        },
        isBtnClicked(commentId){
        //클릭된 버튼의 커멘트 id
            return this.clickedBtn === commentId
        },
        addList(commentId){
            if(this.clickedBtn){
                this.clickedBtn = null
            } else {
                this.clickedBtn = commentId
            }
            axios({
                url: `http://127.0.0.1:8000/articles/comments/${commentId}/`,
                headers: {
                    Authorization: `Token ${this.$store.state.token}`
                },
            })
            .then((response)=>{
                this.content = response.data.content
            })
        },
        updateComment(commentId){
            const content = this.content
            axios({
                method: 'put',
                url: `http://127.0.0.1:8000/articles/comments/${commentId}/`,
                headers: {
                    Authorization: `Token ${this.$store.state.token}`
                },
                data: {
                    content
                }
            })
            .then(()=>{
                this.$store.dispatch('getCommentList', this.articleId)
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