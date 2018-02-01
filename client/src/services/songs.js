import api from '@/services/api'

export default {
  index (search) {
    return api().get('songs' + "?search=" + search)
  },
  create (song) {
    return api().post('songs/', song)
  },
  show (songId) {
    return api().get('songs/' + songId)
  },
  delete (songId) {
    return api().delete('songs/delete/' + songId)
  },
  update (song) {
    return api().put('songs/update/' + song.id, song)
  },
  search (query) {
    console.log(query)
    return api().post('songs/search/', query)
  }
}
