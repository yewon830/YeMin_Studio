<template>
  <div id="app">
    <nav class="navbar">
      <div class="d-flex">
        <div>
          <router-link :to="{name:'HomeView'}" style="color: #3395f4;">YeMin TV</router-link>
        </div>
        <div>
          <router-link :to="{name:'MovieView', params:{page:1}}">영화</router-link>
          <router-link :to="{name:'test'}">test</router-link>
        </div>
        <div>
          <SearchForm/>
          <router-link :to="{name:'SignUpView'}">회원가입</router-link>
          <router-link :to="{name:'LoginView'}">로그인</router-link>
        </div>


      </div>
    </nav>
    <router-view/>
  </div>
</template>

<script>
import SearchForm from '@/components/SearchForm.vue'
export default {
  name: 'App',
  components: {
    SearchForm
  }
}
</script>

<style>
#app {
  font-family: Pretendard, -apple-system, BlinkMacSystemFont, system-ui, Roboto, "Helvetica Neue", "Segoe UI", "Apple SD Gothic Neo", "Noto Sans KR", "Malgun Gothic", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", sans-serif !important;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: whitesmoke;
}

nav {
  padding: 30px;
  color: #999c9f;
  
}

nav a {
  font-weight: bold;
  color: #a8acb3;
  text-decoration: none;
  margin: 20px;
  height: 100%;
  white-space: nowrap;
  font-size: 20px;
  color: #999c9f;
}

nav a.router-link-exact-active {
  color: #42b983;
}

body {
  background-color: #060d17;
}
</style>


