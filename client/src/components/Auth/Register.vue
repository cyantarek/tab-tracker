/* eslint-disable */

<template>
  <v-layout>
    <v-flex xs5 offset-xs3>
      <panel title="Register">
        <v-text-field label="Username" v-model="username"/>
        <v-text-field label="Email" v-model="email"/>
        <v-text-field v-model="password" label="Password" type="password"/>
        <v-text-field v-model="password2" label="Confirm Password" type="password"/>
        <v-btn class="cyan" @click="register" dark>Register</v-btn>
        <p style="color: crimson; font-size: 20px" v-if="err" v-for="e in err">{{ e[0] }}</p>
      </panel>
    </v-flex>
  </v-layout>
</template>

<script>
  import auth from '@/services/auth'


  export default {
    components: {
    },
    data() {
      return {
        username: '',
        password: '',
        password2: '',
        email: '',
        err: '',
      }
    },
    methods: {
      async register() {
        try {
          const response = await auth.register({
            username: this.username,
            email: this.email,
            password: this.password,
            password2: this.password2
          })
          console.log(response.data)
          this.$store.dispatch('setToken', response.data.token)
          this.$store.dispatch('setUser', response.data.user)
          this.$router.push('login')
        } catch (e) {
          console.log(e.response.data)
          this.err = e.response.data
        }
      }
    }
  }
</script>
<style scoped>

</style>
