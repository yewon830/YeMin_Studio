<template>
  <div>
    <router-link :to="{name:'ArticleDetailView', params:{articleId:article.id}}">
    <span>{{article.title}}</span>
    </router-link>
    <span>작성자 : {{article.username}}</span>
    
  </div>
</template>

<script>
export default {
    name: 'ArticleItem',
    props: {
        article : Object
    }
}
</script>

<style>

</style>