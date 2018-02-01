<template>
  <v-layout>
    <v-flex xs4>
      <panel title="Song Metadata">
        <v-text-field label="Title" v-model="song.title" required :rules="[rules.required]"/>
        <v-text-field label="Artist" v-model="song.artist" required :rules="[rules.required]"/>
        <v-text-field label="Genre" v-model="song.genre" required :rules="[rules.required]"/>
        <v-text-field label="Album" v-model="song.album" required :rules="[rules.required]"/>
        <v-text-field label="Album Image" v-model="song.album_image" required :rules="[rules.required]"/>
        <v-text-field label="Youtube ID" v-model="song.youtube_id" required :rules="[rules.required]"/>
      </panel>
    </v-flex>
    <v-flex xs8>
      <panel title="Song Structure" class="ml-2">
        <v-text-field label="Tab" v-model="song.tab" multi-line required :rules="[rules.required]"/>
        <v-text-field label="Lyrics" v-model="song.lyrics" multi-line required :rules="[rules.required]"/>
      </panel>
      <div class="danger-alert" v-if="error">{{error}}</div>
      <v-btn class="cyan" @click="save" dark>Save</v-btn>
    </v-flex>
  </v-layout>
</template>

<script>
  import song from '@/services/songs'

  export default {
    components: {
    },
    name: "create-song",
    data() {
      return {
        song: {},
        error: null,
        rules: {
          required: (value) => !!value || 'Required'
        }
      }
    },
    methods: {
      async save() {
        this.error = null
        const areAllFilled = Object
          .keys(this.song)
          .every(key => !!this.song[key])
        if (!areAllFilled) {
          this.error = 'Please fill in all required fields'
          return
        }
        try {
          const response = await song.update(this.song)
          console.log(response.data)
          this.$router.push({
            name: 'view-song'
          , params:  {songId: this.song.id}})
        } catch (e) {
          this.err = e.response.data
        }

      }
    },
    async mounted () {
          const songId = this.$store.state.route.params.songId
          const response = await song.show(songId)
          this.song = response.data
    }
  }
</script>

<style scoped>
  .danger-alert {
    color: red;
    font-family: Roboto;
    font-size: 25px;
  }
</style>
