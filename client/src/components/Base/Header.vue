<template>
  <v-toolbar fixed color="cyan" dark>
    <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
    <v-toolbar-title class="mr-4">
      <router-link tag="span" class="home" :to="{name: 'home'}">SongBook</router-link>
    </v-toolbar-title>
    <v-toolbar-items>
      <v-btn dark flat :to="{name: 'songs'}">
        Browse
      </v-btn>
    </v-toolbar-items>
    <v-toolbar-items>
      <v-btn dark flat :to="{name: 'song-create'}">
        Add
      </v-btn>
    </v-toolbar-items>
    <v-toolbar-items>
      <v-btn dark flat :to="{name: 'about'}">
        About
      </v-btn>
    </v-toolbar-items>
    <v-spacer></v-spacer>
    <v-toolbar-items>
      <v-btn dark flat :to="{name: 'login'}" v-if="!$store.state.isUserLoggedIn">
        Login
      </v-btn>
    </v-toolbar-items>
    <v-toolbar-items>
      <v-btn dark flat :to="{name: 'register'}" v-if="!$store.state.isUserLoggedIn">
        Signup
      </v-btn>
    </v-toolbar-items>
    <v-toolbar-items>
      <v-btn dark flat v-if="$store.state.isUserLoggedIn">{{$store.state.user.username}}</v-btn>
    </v-toolbar-items>
    <v-toolbar-items>
      <v-btn dark flat @click="logout" v-if="$store.state.isUserLoggedIn">
        Logout
      </v-btn>
    </v-toolbar-items>
  </v-toolbar>
</template>

<script>
  export default {
    name: 'header',
    methods: {
      logout() {
        this.$store.dispatch('setToken', null)
        this.$store.dispatch('setUser', null)
        this.$router.push({
          name: 'home'
        })
      }
    },
    components: {}
  }
</script>

<style scoped>
  .home {
    cursor: pointer;
  }
</style>
