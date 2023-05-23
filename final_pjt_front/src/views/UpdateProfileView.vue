<template>
  <div>
    <h1>회원정보 변경</h1>
    <form @submit.prevent="updateProfileImage">
      <p>프로필 사진</p>
    </form>

    <form @submit.prevent="updateProfile">
        <p>닉네임</p>
        <input type="text" v-model="username">
        <p>이메일</p>
        <input type="email" v-model="email">
        <p>비밀번호</p>
        <input type="password" v-model="password1">
        <p>비밀번호 확인</p>
        <input type="password" v-model="password2">
        <button>변경</button>
    </form>
  </div>
</template>

<script>
export default {
    name : 'UpdateProfileView',
    data(){
      return{
        password1: null,
        password2: null,
        email: null,
        username: null,
      }

    },
    methods: {
      updateProfile(){
        const username = this.username
        const password1 = this.password1
        const password2 = this.password2
        const email = this.email
        const payload = {
          username, email, password1,password2
        }
        this.$store.dispatch('updateProfile', payload)
      }
    }
}
</script>

<style>

</style>