<template>
  <v-layout row>
    <v-flex xs4 class="mr-2">
      <recent-views></recent-views>
      <bookmarked></bookmarked>
    </v-flex>
    <v-flex xs8>
      <search></search>
      <song-list></song-list>
    </v-flex>
  </v-layout>
</template>

<script>
  import Search from '@/components/Search'
  import RecentViews from '@/components/RecentViews'
  import Bookmarked from '@/components/Bookmarked'
  import SongList from '@/components/Song/SongList'

  export default {
    name: 'songs',
    components: {
      Search,
      RecentViews,
      Bookmarked,
      SongList
    }
  }
</script>

<style scoped>

</style>
