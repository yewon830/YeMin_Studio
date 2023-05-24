<template>
  <div>
    <h1>회원정보 변경</h1>
    <form @submit.prevent="updateProfile">
        <p>닉네임</p>
        <input type="text" v-model="nickname">
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
        nickname: null,
      }
    },
    // computed : {
    //   originUserProfile(){
    //     return this.$store.state.userProfile
    //   }
    // },  
    created(){
      this.getUserProfile()
    },
    methods: {
      getUserProfile(){
            this.$store.dispatch('getUserProfile')
            const userProfile = this.$store.state.userProfile
            this.email = userProfile.email
            this.nickname = userProfile.nickname
      },
      updateProfile(){
        if(this.password1!= this.password2){
          alert('패스워드가 일치하지 않습니다')
          return
        }
        if(!this.password1){
          alert('패스워드를 입력해주세요')
          return
        }
        if(!this.password2){
          alert('패스워드 확인을 해주세요.')
          return
        }
        if(!this.nickname){
          alert('닉네임을 입력해주세요.')
          return
        }
        const nickname = this.nickname
        const password1 = this.password1
        const password2 = this.password2
        const email = this.email
        const payload = {
          nickname, email, password1,password2
        }
        this.$store.dispatch('updateProfile', payload)
          .then(() => {
            this.$router.push({ name : 'ProfileView' })
          })
          .catch((error) => {
            console.log(error)
          })
      }
    }
}
</script>

<style>

</style>