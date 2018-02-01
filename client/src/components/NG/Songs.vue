<template>
  <v-layout>
    <v-flex xs4 class="mr-2">
      <div class="white">
        <v-toolbar color="cyan" dark>
          <v-toolbar-title>Recently Viewed Songs</v-toolbar-title>
        </v-toolbar>
      </div>

      <div class="white elevation-1 mt-2">
        <v-toolbar color="cyan" dark>
          <v-toolbar-title>Bookmarked Songs</v-toolbar-title>
        </v-toolbar>

      </div>

    </v-flex>

    <v-flex xs8>
      <div class="white elevation-1 mb-2">
        <v-toolbar color="cyan" dark>
          <v-toolbar-title>Search for Songs</v-toolbar-title>
        </v-toolbar>
        <div>
          <v-text-field label="Search for Songs, Artists, Albums or Genre" v-model="username"/>
        </div>
      </div>

      <div class="white elevation-1">
        <v-toolbar color="cyan" dark>
          <v-toolbar-title>Songs</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-toolbar-items>
            <v-btn dark large dark absolute middle right class="cyan accent-3"
                   @click="navigateTo({name: 'song-create'})">
              Add
            </v-btn>
          </v-toolbar-items>
        </v-toolbar>
        <div v-for="song in songs" class="songs">
          <v-layout>
            <v-flex xs6>
              <div class="song-title">{{song.title}}</div>
              <div class="song-artist">{{song.artist}}</div>
              <div class="song-album">{{song.album}}</div>
              <v-btn dark class="cyan" @click="navigateTo({name: 'view-song', params: {songId: song.id}})">View Song
              </v-btn>
              <v-btn dark class="red" @click="navigateTo({name: 'delete-song', params: {songId: song.id}})">Delete Song
              </v-btn>
            </v-flex>
            <v-flex xs6>
              <img class="album-image" :src="song.album_image"/>
            </v-flex>
          </v-layout>

        </div>
      </div>
    </v-flex>
  </v-layout>
</template>

<script>
  import Songs from '@/services/songs'

  export default {
    name: 'songs',
    data() {
      return {
        songs: []
      }
    },
    async mounted() {
      try {
        const response = await Songs.index()
        this.songs = response.data
      } catch (e) {

      }

    },
    methods: {
      navigateTo(route) {
        this.$router.push(route)
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

  .album-image {
    width: 70%;
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
