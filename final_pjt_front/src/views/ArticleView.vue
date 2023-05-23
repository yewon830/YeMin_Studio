<template>
  <div>
    <h1>Article</h1>
    <router-link :to="{name:'ArticleCreateView'}">글 작성하기</router-link>
    <ArticleList/>
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList'
export default {
    name: 'ArticleView',
    components: {
        ArticleList,
    },

}
</script>

<style>

</style>