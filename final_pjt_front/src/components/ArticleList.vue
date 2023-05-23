<template>
  <div>
    
    <ArticleItem  v-for="article in articleList" :key="article.id"/>
  </div>
</template>

<script>
import ArticleItem from '@/components/ArticleItem'
export default {
    name: 'ArticleList',
    components:{
        ArticleItem
    },
    computed: {
        articleList(){
            return this.$store.state.articleList
        }
    }
}
</script>

<style>

</style>