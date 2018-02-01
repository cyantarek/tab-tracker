<template>
  <v-layout>
    <v-flex xs5 offset-xs3>
      <panel title="Delete Song">
        <v-layout>
          <v-flex xs12>
            <div class="song-title" style="color: grey; font-size: 250%">Are you sure you want to delete</div>
            <div class="song-title">{{song.title}}?</div>
            <v-btn class="red" @click="del" dark>Yes</v-btn>
            <v-btn class="cyan" @click="navigateTo({'name': 'songs'})" dark>No</v-btn>
          </v-flex>
        </v-layout>
      </panel>
    </v-flex>
  </v-layout>
</template>

<script>
  import song from '@/services/songs'


  export default {
    name: "view-song",
    data() {
      return {
        song: {}
      }
    },
    async mounted() {
      const songId = this.$store.state.route.params.songId
      const response = await song.show(songId)
      this.song = response.data
      console.log(response.data)
    },
    methods: {
      async del() {
        const songId = this.$store.state.route.params.songId
        const response = await song.delete(songId)
        this.$router.push({
          name: 'songs'
        })
      },
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
    font-size: 24px;
    padding: 0px;
    color: #00bbd3;
  }
</style>
