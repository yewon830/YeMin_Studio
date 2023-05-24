<template>
  <div class="sign-up-page">
    <a href="http://localhost:8080/">YeMin TV</a>
    <div class="sign-up-box">
        <div>회원가입</div>
        <form @submit.prevent="signUp" style="text-align: start;">
            <div>
                <label>아이디 </label>
            </div>
            <div class="input-box">
                <input type="text" v-model="username" placeholder="아이디를 입력해주세요">
            </div>
            <div>
                <label>닉네임 </label>
            </div>
            <div class="input-box">
                <input type="text" v-model="nickname" placeholder="닉네임을 입력해주세요">
            </div>

            <div>
                <label>이메일 </label>
            </div>
            <div class="input-box">
                <input type="email" v-model="email" placeholder="example@gmail.com" autocomplete="email" autocapitalize="none" spellcheck="false">
            </div>

            <div>
                <label>비밀번호 </label>
            </div>
            <div class="input-box">
                <input type="password" v-model="password1" placeholder="비밀번호를 입력해주세요" autocapitalize="off" spellcheck="false">
            </div>
            <div>
                <label>비밀번호 확인 </label>
            </div>
            <div class="input-box">
                <input type="password" v-model="password2" placeholder="비밀번호를 다시 입력해주세요" autocapitalize="off" spellcheck="false">
            </div>
             <button class="btn btn-primary">확인</button>
           

        </form>

    </div>
  </div>
</template>

<script>
export default {
    name: 'SignUpView',
    data(){
        return {
            username: null,
            nickname: null,
            email: null,
            password1: null,
            password2: null,
        }
    },
    methods: {
        signUp(){
            const username = this.username
            const nickname = this.nickname
            const email = this.email
            const password1 = this.password1
            const password2 = this.password2

            const payload = {
                username, nickname, email, password1, password2
            }
            this.$store.dispatch('signUp',payload)
        }
    }
}
</script>

<style>
.sign-up-page{
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
.sign-up-box{
    background-color: white;
    padding: 2rem;
    border: 1px solid lightgray;
    width: 386px;
    border-radius: 0.25rem;
}
input{
    border: none;
    outline: none;
    caret-color: #3395f4;
}

.input-box{
    display: flex;
    margin-top: 0.5rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid lightgray;
    margin-bottom: 1.5rem;
}

</style>