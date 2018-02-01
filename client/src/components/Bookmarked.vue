<template>
  <panel title="Bookmarked Songs" class="mb-2">
    <v-data-table :headers="headers" :pagination.sync="pagination" :items="bookmarks" class="elevation-1">
      <template slot="items" scope="props">
        <td class="text-xs-left" style="font-size: 150%; color: #00bbd3;">
          {{props.item.song}}
        </td>
      </template>
    </v-data-table>
  </panel>
</template>

<script>
  import bookmark from '@/services/bookmarks'

  export default {
    name: 'bookmarked',
    data() {
      return {
        headers: [
          {
            text: "Song",
            value: "song"
          },
          {
            text: "User",
            value: "user"
          },
        ],
        pagination: {
          sortBy: "id",
          descending: true
        }
      }
    },
    components: {},
    data() {
      return {
        bookmarks: []
      }
    },
    async mounted() {
      const user_id = this.$store.state.user.id
      this.bookmarks = (await
          bookmark.get({userId: user_id})
      ).data
      console.log(this.bookmarks)
    },
  }
</script>

<style scoped>

</style>
