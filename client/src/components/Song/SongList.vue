<template>
  <panel title="Songs">
    <div v-for="song in songs" class="songs">
      <v-layout>
        <v-flex xs6>
          <div class="song-title">{{song.title}}</div>
          <div class="song-artist">{{song.artist}}</div>
          <div class="song-album">{{song.album}}</div>
          <v-btn dark class="indigo accent-2" @click="navigateTo({name: 'view-song', params: {songId: song.id}})">View
          </v-btn>
          <v-btn dark class="red" @click="navigateTo({name: 'delete-song', params: {songId: song.id}})">Delete
          </v-btn>
        </v-flex>
        <v-flex xs6>
          <img class="album-image" :src="song.album_image"/>
        </v-flex>
      </v-layout>
      <hr>
    </div>
  </panel>
</template>

<script>
  import Songs from '@/services/songs'

  export default {
    name: 'song-list',
    components: {},

    data() {
      return {
        songs: [],
      }
    },
    async mounted() {
    },
    methods: {
      navigateTo(route) {
        this.$router.push(route)
      }
    },
    watch: {
      '$route.query.search': {
        immediate: true,
        async handler (value) {
          this.songs = (await
          Songs.index(value)).data
        }
      }
    }
  }
</script>

<style scoped>

  .song-artist {
    padding: 40px;
    height: 30px;
    overflow: hidden;
    color: #00bbd3;
  }

  hr {
    display: block;
    height: 1px;
    border: 0;
    border-top: 1px dashed #00bbd3;
    margin: 1em 0;
    padding: 0;
  }

  .album-image {
    width: 50%;
    margin: 0 auto;
    padding: 10px;

  }

  .song-title {
    font-size: 50px;
    color: #00bbd3;
  }

  .song-genre {
    font-size: 18px;
    color: #00bbd3;
  }

  .song-artist {
    font-size: 24px;
    padding: 0px;
    color: #00bbd3;
  }

  .song-album {
    font-size: 20px;
    padding: 0px;
    color: rgba(130, 107, 92, 0.62);
  }
</style>
