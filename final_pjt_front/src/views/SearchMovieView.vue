<template>
  <div>
    <h1 class="text-start m-4">'{{ this.$route.params.keyword }}' 검색 결과</h1>
    <div class="d-flex container-fluid row row-cols-1 row-cols-md-6 g-4">
        <SearchMovieItem v-for="movie in movies" :key="movie.title" :movie="movie"/>
    </div>
  </div>
  
</template>

<script>
import SearchMovieItem from '@/components/SearchMovieItem'
import axios from 'axios'
export default {
    name: 'SearchMovieView',
    components:{
        SearchMovieItem
    },
    data(){
        return {
            movies : null
        }
    },
    created(){
        this.getSearchMovies()
    },
    methods: {
        getSearchMovies(){
            axios({
                url: `http://127.0.0.1:8000/movies/${this.$route.params.keyword}/`
            })
            .then((response)=>{
                this.movies = response.data
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