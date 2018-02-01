<template>
  <panel :title="title" class="mr-2 mb-2">
    <v-layout>
      <v-flex xs6>
        <div class="song-title">{{song.title}}</div>
        <div class="song-artist">{{song.artist}}</div>
        <div class="song-album">{{song.album}}</div>
        <div class="song-genre">{{song.genre}}</div>
        <v-btn class="indigo darken-2" @click="navigateTo({name: 'edit-song', params: {songId: song.id}})" dark>Edit</v-btn>
        <v-btn class="deep-purple darken-1" @click="setAsBookmark" dark v-if="$store.state.isUserLoggedIn && !bookmark">
          Bookmark
        </v-btn>
        <v-btn class="red" @click="removeBookmark" dark v-if="$store.state.isUserLoggedIn && bookmark">
          UnBookmark
        </v-btn>
      </v-flex>
      <v-flex xs6>
        <img class="album-image" :src="song.album_image"/>
      </v-flex>

    </v-layout>

  </panel>
</template>

<script>
  import Panel from '@/components/base/Panel'
  import songs from "../../../services/songs";
  import bookmarks from "../../../services/bookmarks";

  export default {
    name: "song-metadata",
    components: {
      Panel
    },
    data() {
      return {
        bookmark: null
      }
    },
    props: [
      'song',
      'title'
    ],
    watch: {
      async song() {
        const response = await bookmarks.get({
          songId: this.song.id,
          userId: this.$store.state.user.id
        })
        this.bookmark = response.data
      }
    },
    methods: {
      navigateTo(route) {
        this.$router.push(route)
      },
      async setAsBookmark() {
        try {
          this.bookmark = (await bookmarks.create({
            songId: this.$route.params.songId,
            userId: this.$store.state.user.id
          })).data
        } catch (e) {
          console.log(e.data)
        }
      },
      async removeBookmark() {
        try {
          await bookmarks.delete({id: this.bookmark.id})
          this.bookmark = null
        } catch (e) {
          console.log(e)
        }
      }
    },
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
