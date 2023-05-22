<template>
  <div>
    <h1>회원정보 변경</h1>
    <form @submit.prevent="updateUsername">
        <p>닉네임</p>
        <input type="text">
    </form>
    <p>이메일</p>
    <input type="email">
    <p>비밀번호</p>
    <input type="password">
  </div>
</template>

<script>
export default {
    name : 'UpdateProfileView',
    data(){

    }
}
</script>

<style>

</style>