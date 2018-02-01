/* eslint-disable */

<template>
  <v-layout>
    <v-flex xs5 offset-xs3>
      <panel title="Login">
        <v-text-field label="Username" v-model="username"/>
        <v-text-field v-model="password" label="Password" type="password"/>
        <div style="color: crimson;font-size: 20px" v-if="err" v-for="e in err">{{ e[0] }}</div>
        <v-btn class="cyan" @click="login" dark>Login</v-btn>
      </panel>
    </v-flex>
  </v-layout>
</template>

<script>
  import login from '@/services/login'

  export default {
    components: {
    },
    data() {
      return {
        username: '',
        password: '',
        msg: '',
        err: '',
        token: '',
      }
    },
    methods: {
      async login() {
        try {
          const response = await login.login({
            username: this.username,
            password: this.password
          })
          this.$store.dispatch('setToken', response.data.token)
          this.$store.dispatch('setUser', response.data)
          this.$router.push({
            name: 'songs'
          })
        } catch (e) {
          console.log(e.response.data)
          this.err = e.response.data
          this.msg = ''
        }
      }
    }
  }
</script>
