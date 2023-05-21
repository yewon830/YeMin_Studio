<template>
  <div class="login-page">
    <a href="http://localhost:8080/">YeMin TV</a>
    <div class="login-box">
        <form @submit.prevent="login">
            <div>
                <label>이메일</label>
            </div>
            <div class="input-box">
                <input name="email" type="email" v-model="email" autocomplete="email" autocapitalize="none" spellcheck="false">
            </div>
            <div>
                <label>비밀번호</label>
            </div>
            <div class="input-box">
                <input name="password" v-model="password" type="password" autocapitalize="off">
            </div>
            <button class="btn btn-primary">확인</button>
        </form>
    </div>
  </div>
</template>

<script>
export default {
    name:'LoginView',
    data(){
        return {
            email: null,
            password: null,
        }
    },
    methods: {
        login(){
            const email = this.email
            const password = this.password

            const payload = {
                email,password
            }
            this.$store.dispatch('login',payload)
        }
    }
    
}
</script>

<style>
.login-page{
    padding-top: 2rem;
    padding-bottom: 2rem;
    width: 100%;
    min-height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    -webkit-box-align: center;
    flex-direction: column;
    color: rgb(61, 61, 61);
}
.login-box{
    background-color: white;
    padding: 2rem;
    border: 1px solid lightgray;
    width: 386px;
    border-radius: 0.25rem;
    text-align: start;
}

.input-box{
    display: flex;
    margin-top: 0.5rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid lightgray;
    margin-bottom: 1.5rem;
}
</style>