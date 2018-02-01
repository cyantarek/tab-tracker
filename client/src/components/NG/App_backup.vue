<template>
  <div id="app">
    <v-app>
          <page-header></page-header>
      <main>
        <v-container fluid>
              <router-view/>
        </v-container>
      </main>
    </v-app>
  </div>
</template>

<script>
  import PageHeader from '@/components/Header'
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
</style>
