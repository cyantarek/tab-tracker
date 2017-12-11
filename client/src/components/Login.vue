/* eslint-disable */

<template>
  <div>
    <h1>Login</h1>

    <input type="text" name="username" placeholder="Username" v-model="username">
    <input type="password" name="password" placeholder="Password" v-model="password">
    <button @click="login">Login</button>
    <p style="color: crimson" v-if="msg">*{{ msg }}</p>
  </div>
</template>

<script>
  import auth from '@/services/login'

  export default {
    data () {
      return {
        username: '',
        password: '',
        msg: ''
      }
    },
    methods: {
      async login () {
        try {
          const response = await auth.login({
            username: this.username,
            password: this.password
          })
          console.log(response.data)
          this.msg = 'User registered successfully'
          this.username = ''
          this.password = ''
        } catch (e) {
          console.log(e.response.data)
          this.msg = e.response.data
        }
      }
    }
  }
</script>
