import api from '@/services/api'

export default {
  get (params) {
    return api().get('bookmarks', {params: params})
  },
  create (params) {
    return api().post('bookmarks/add/', params)
  },
  delete (data) {
    return api().delete('bookmarks/delete/', {data: data})
  }
}
