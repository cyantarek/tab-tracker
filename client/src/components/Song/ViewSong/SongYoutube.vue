<template>
    <panel title="Youtube Video" class="mb-2">
      <youtube :video-id="song.youtube_id" player-width="540" player-height="360"></youtube>
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

</style>
