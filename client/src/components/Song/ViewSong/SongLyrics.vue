<template>
  <panel title="Lyrics" class="mb-2">
    <textarea readonly label="Lyrics" v-model="song.lyrics" multi-line/>
  </panel>
</template>

<script>
  import Panel from '@/components/base/Panel'

  export default {
    name: "song-lyrics",
    components: {
      Panel
    },
    props: [
      'song'
    ]
  }
</script>

<style scoped>


  textarea {
    width: 100%;
    font-family: monospace;
    border: none;
    height: 600px;
    border-style: none;
    border-color: transparent;
    overflow: auto;
    padding: 40px;

  }

</style>
