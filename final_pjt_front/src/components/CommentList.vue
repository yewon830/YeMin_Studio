<template>
  <div>
    <div>
        <div v-for="(comment) in comments" :key="comment.id">
                <strong><span style="font-size: 18px; margin-left: 20px; color:rgba(21, 21, 211, 0.87)"> {{comment.username}}</span></strong>
                <span style="font-size: 16px; margin-left: 10px; margin-bottom: 10px;">{{comment.content}}</span>
        <div v-if="currentUsername === comment.username" style="margin-bottom: 20px;">
            <button class="btn btn-outline-primary" @click="addList(comment.id)">수정</button>
            <div v-if="isBtnClicked(comment.id)">
                <form @submit.prevent="updateComment(comment.id)">
                    <input class="comment-input" type="text" v-model="content" style="width: 500px; height: 80px;">
                    <button class="btn btn-primary">작성</button>
                </form>
            </div>
            <button class="btn btn-outline-primary" style="margin-left: 10px;" @click="deleteComment(comment.id)">삭제</button>
        
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