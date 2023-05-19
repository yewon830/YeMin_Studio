<template>
  <div>
    <h1>-{{ this.$route.params.keyword }}- 검색한 결과</h1>

    <div v-for="movie in movies" :key="movie.title">
        <p>
            {{movie.title}}
        </p>
    </div>
  </div>
  
</template>

<script>
import axios from 'axios'
export default {
    name: 'SearchMovieView',
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
        // getSearchMovies(){
        //     axios({
        //         url: 'https://api.themoviedb.org/3/movie/top_rated?api_key=cdb84e32fe9892b6b1fad1b2dceb89d0&language=ko-KR&page=1',
        //     })
        //     .then((response)=>{
        //         const testmovies = response.data.results
        //         const movieList = []
        //         for (const movie of testmovies){
        //             if (movie.title.includes(this.$route.params.keyword)|| movie.overview.includes(this.$route.params.keyword)){
        //                 movieList.push(movie)
        //             }
        //         }
        //         this.movies = movieList
        //     })
        //     .catch((err)=>{
        //         console.log(err)
        //     })
        // }
    }
}


</script>

<style>

</style>