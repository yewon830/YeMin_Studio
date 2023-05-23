<template>
  <div>

    <ArticleItem  v-for="article in articleList" :key="article.id" :article="article"/>
  </div>
</template>

<script>
import ArticleItem from '@/components/ArticleItem'
export default {
    name: 'ArticleList',
    components:{
        ArticleItem
    },
    computed:{
      articleList(){
        return this.$store.state.articleList
      }
    },
   created(){
        this.getArticleList()
    },
    methods: {
        getArticleList(){
          
            this.$store.dispatch('getArticleList')
        }
    }
}
</script>

<style>

</style>