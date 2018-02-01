<template>
  <div id="app">
    <v-app>
      <page-header></page-header>
      <main>
        <v-container fluid>
          <router-view/>
        </v-container>
      </main>
      <v-footer color="cyan" app>
        <v-footer-title>
          <span class="white--text">&copy; 2017 - Developed at Big Idea Software, Developer - Cyan Tarek</span>
        </v-footer-title>
      </v-footer>
    </v-app>
  </div>
</template>

<script>
  import PageHeader from '@/components/Base/Header'

  export default {
    name: 'app',

    components: {
      PageHeader
    }
  }
</script>

<style>
  #app {
    font-family: 'Roboto', "Roboto Lt", "Roboto Lt", sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  body {
    padding-top: 80px;
  }

</style>
