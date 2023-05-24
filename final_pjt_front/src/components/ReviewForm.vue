<template>
  <div>
    <form @submit.prevent="onSubmit">
        <input type="text" placeholder="리뷰를 작성해주세요">
        <button>작성</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {

    name: 'ReviewForm',
    props:{
        movieId: Number
    },
    data(){
        return{
            content: null
        }
    },
    methods: {
        onSubmit(){
            const content = this.content
            if(!this.content){
                alert('리뷰를 작성해주세요')
                return
            }
            axios({
                method: 'post',
                url: `http://127.0.0.1:8000/movies/reviews/create/`,
                headers: {
                    Authorization: `Token ${this.$store.state.token}`
                },
                data: {content}
            })
            .then(()=>{
                this.$store.dispatch()
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