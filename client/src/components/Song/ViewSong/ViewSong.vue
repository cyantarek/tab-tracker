<template>
  <v-layout fluid>
    <v-flex xs3 offset-xs4 v-if="error">
      <panel title="Sorry">
        <div class="song-title">Sorry! Your requested song not found!</div>
      </panel>
    </v-flex>
    <v-flex xs6 v-if="!error">
      <song-metadata :song="song" title="Song Metadata"></song-metadata>
      <song-tabs :song="song"></song-tabs>
    </v-flex>
    <v-flex xs6 v-if="!error">
      <song-lyrics :song="song"></song-lyrics>
      <song-youtube :song="song"></song-youtube>
    </v-flex>
  </v-layout>
</template>

<script>
  import song from '@/services/songs'
  import VueYoutubeEmbed from 'vue-youtube-embed'
  import Panel from '@/components/Base/Panel'
  import SongMetadata from '@/components/Song/ViewSong/SongMetadata'
  import SongTabs from '@/components/Song/ViewSong/SongTabs'
  import SongLyrics from '@/components/Song/ViewSong/SongLyrics'
  import SongYoutube from '@/components/Song/ViewSong/SongYoutube'

  export default {
    name: 'view-song',
    components: {
      Panel,
      SongMetadata,
      SongTabs,
      SongLyrics,
      SongYoutube
    },
    data() {
      return {
        song: {},
        error: false,
      }
    },
    async mounted() {
      try {
      const songId = this.$store.state.route.params.songId
      const response = await song.show(songId)
      this.song = response.data
      } catch (e) {
        this.error = true
      }

    }
  }
</script>

<style scoped>
.song-title {
    font-size: 50px;
    color: #00bbd3;
  }
</style>

