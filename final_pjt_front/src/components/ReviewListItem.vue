<template>
  <div>
    <span>{{review.content}}</span> - <span>작성자:{{review.user.username}}</span>
    <button @click="isBtnClicked">수정하기</button> 
    
    <button>삭제하기</button>
    <hr>
  </div>
</template>

<script>
export default {
    name: 'ReviewListItem',
    props : {
        review: Object
    },
    methods:{
        isBtnClicked(){
            
        }
    }
}
</script>

<style>

</style>