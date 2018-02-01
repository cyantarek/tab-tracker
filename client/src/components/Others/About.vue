<template>
  <v-layout>
    <v-flex xs5 offset-xs3>
      <panel title="About Me">
        <v-layout>
          <v-flex xs12>
            <div style="font-size: 200%; text-align: left">Software: SongBook</div>
            <div style="font-size: 200%;text-align: left">Developer/Engineer: Cyan Tarek</div>
            <div style="font-size: 200%;text-align: left">Facebook: Cyan Tarek</div>
            <div style="font-size: 200%;text-align: left;color: #00bbd3;">Technology stack:</div>
            <div style="font-size: 200%;text-align: left">Frontend: Vuejs, Vuex, Vuerouter, axios</div>
            <div style="font-size: 200%;text-align: left">Backend: Python/Django, Djago REST</div>
            <div style="font-size: 200%;text-align: left">Database: PostgreSQL</div>
            <v-btn class="red" @click="" dark>Thanks</v-btn>
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
