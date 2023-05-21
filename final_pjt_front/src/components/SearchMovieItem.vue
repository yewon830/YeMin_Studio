<template>
  <div>
    <a :href="`http://localhost:8080/movies/detail/${movie.id}`">
        <img :src="`https://image.tmdb.org/t/p/w200${movie.poster_path}`" style="height: 285px; width: 200px" class="rounded" :alt="`${movie.title}`">
        <p>{{movie.title}}</p>
    </a>
  </div>
</template>

<script>
export default {
    name: 'SearchMovieItem',
    props: {
        movie: Object
    }
}
</script>

<style>

</style>