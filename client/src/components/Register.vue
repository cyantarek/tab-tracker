/* eslint-disable */

<template>
  <div>
    <h1>Register</h1>

    <input type="text" name="username" placeholder="Username" v-model="username">
    <input type="text" name="email" placeholder="Email" v-model="email">
    <input type="password" name="password" placeholder="Password" v-model="password">
    <input type="password" name="password2" placeholder="Confirm Password" v-model="password2">
    <button @click="register">Register</button>
    <p style="color: crimson" v-if="msg">*{{ msg }}</p>
  </div>
</template>

<script>
  import auth from '@/services/auth'
  export default {
    data () {
      return {
        username: '',
        password: '',
        password2: '',
        email: '',
        msg: ''
      }
    },
    methods: {
      async register () {
        try {
          const response = await auth.register({
            username: this.username,
            email: this.email,
            password: this.password,
            password2: this.password2
          })
          console.log(response.data)
          this.msg = 'User registered successfully'
          this.username = ''
          this.email = ''
          this.password = ''
          this.password2 = ''
        } catch (e) {
          console.log(e.response.data)
          this.msg = e.response.data
        }
      }
    }
  }
</script>
