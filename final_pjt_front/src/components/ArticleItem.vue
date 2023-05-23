<template>
  <div>
    <router-link :to="{name:'ArticleDetailView', params:{articleId:article.id}}">
    <h5>{{article.title}}</h5>
    </router-link>
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