<template>
  <div>
    <h1>히히히</h1>
    <form @submit.prevent="commentCreate">
        <input type="text" v-model="content">
        <button>작성</button>
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
*{
    margin: 0;
    padding: 0;
}
.rate {
    float: left;
    height: 46px;
    padding: 0 10px;
}
.rate:not(:checked) > input {
    position:absolute;
    top:-9999px;
}
.rate:not(:checked) > label {
    float:right;
    width:1em;
    overflow:hidden;
    white-space:nowrap;
    cursor:pointer;
    font-size:30px;
    color:#ccc;
}
.rate:not(:checked) > label:before {
    content: '★ ';
}
.rate > input:checked ~ label {
    color: #ffc700;    
}
.rate:not(:checked) > label:hover,
.rate:not(:checked) > label:hover ~ label {
    color: #deb217;  
}
.rate > input:checked + label:hover,
.rate > input:checked + label:hover ~ label,
.rate > input:checked ~ label:hover,
.rate > input:checked ~ label:hover ~ label,
.rate > label:hover ~ input:checked ~ label {
    color: #c59b08;
}

</style>