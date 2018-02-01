<template>
  <panel title="Search for Songs" class="mb-2">
    <v-text-field label="Search for Songs, Artists, Albums or Genre" v-model="search"/>
  </panel>
</template>

<script>
  import Songs from '@/services/songs'
  import _ from 'lodash'

  export default {
    name: 'search',
    components: {},
    data() {
      return {
        search: ''
      }
    },
    watch: {
      search: _.debounce(async  function (value) {
        const route = {
          name: 'songs'
        }
        if (this.search !== '') {
          route.query = {
            search: this.search
          }
        }
        this.$router.push(route)
      }, 700),
      '$route.query.search': {
        immediate: true,
        handler(value) {
          this.search = value
        }
      }
    },
  }
</script>

<style scoped>

</style>
