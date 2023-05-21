<template>
  <div>
    <div class="movie-info d-flex justify-content-around">
        <div style="width: 60%;">
            <div class="d-flex">
                <h1 class="text-start">{{movie.title}}</h1>
                <div  @click="likeMovie" class="pt-4 mx-4">
                    <font-awesome-icon :color="heartColor" :icon="['fas', 'heart']" size="lg" />
                </div>
                <div  @click="wishMovie" class="pt-4">
                    <font-awesome-icon :color="wishColor" :icon="['fasl', 'folder-open']" size="lg" />
                </div>
            </div>
            
            <div style="min-height: 29.125rem; font-size: 0.875rem;">
                <p class="text-overview">{{movie.overview}}</p>
                <input type="checkbox" class="more-btn">
            </div>
        </div>
        <aside class="d-flex flex-column">
            <div class="d-flex">
                <h6>감독</h6>
                <span>{{movie.director.name}}</span>
            </div>
            <div class="d-flex">
                <h6>배우</h6>
                <div class="d-flex flex-column">
                    <div v-for="actor in movie.actors" :key="actor.name">
                        <span>{{actor.name}}</span>
                    </div>
                </div>
            </div>
            <div class="d-flex">
                <h6>개봉날짜</h6>
                <span>{{movie.release_date}}</span>
            </div>

        </aside>
    </div>
  </div>
</template>

<script>
export default {
    name: 'MovieDetailVideo',
    props: {
        movie: Object
    },
    data(){
        return{
            isHeartClicked: false,
            isWishClicked: false,
            heartColor: 'white',
            wishColor: 'white'
        }
    },
    methods: {
        likeMovie(){
            this.$store.dispatch('likeMovie', this.movie.id)
            this.isHeartClicked = !this.isHeartClicked
            if (this.isHeartClicked === true){
                this.heartColor = '#4590e3'
            } else{
                this.heartColor = 'white'
            }

        },
        wishMovie(){
            this.$store.dispatch('wishMovie', this.movie.id)
            this.isWishClicked = !this.isWishClicked
            if (this.isWishClicked === true){
                this.wishColor = '#4590e3'
            } else{
                this.wishColor = 'white'
            }
        }
    }
    
}
</script>

<style>
.modal,.overlay{
    width: 100%;
    height: 100%;
    position: fixed;
}
.movie-info{
    padding: 40px 40px 40px 40px;
}
.text-overview{
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
    margin-bottom: 0px;
}
.more-btn{
    appearance: none;
    border: none;
    padding: 0.5em;
    cursor: pointer;
}
.more-btn::before{
    content: '더보기';
    color: #4590e3;
}
.more-btn:checked::before{
    content: '닫기';
    color: #4590e3;
}
.text-overview:has(+ .more-btn:checked){
    -webkit-line-clamp:unset;
}
h6{
    margin-right:10px;
}
aside{
    font-size: 0.875rem;
}
aside span{
    color: #d4d7db;
}


</style>