import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Register from '@/components/Auth/Register'
import Login from '@/components/Auth/Login'
import Songs from '@/components/Song/SongsPanel'
import CreateSong from '@/components/Song/CreateSong'
import ViewSong from '@/components/Song/ViewSong/ViewSong'
import DeleteSong from '@/components/Song/DeleteSong'
import EditSong from '@/components/Song/EditSong'
import About from '@/components/Others/About'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/songs',
      name: 'songs',
      component: Songs
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '/songs/create/',
      name: 'song-create',
      component: CreateSong,
    },
    {
      path: '/songs/:songId/',
      name: 'view-song',
      component: ViewSong
    },
    {
      path: '/songs/:songId/delete/',
      name: 'delete-song',
      component: DeleteSong
    },
    {
      path: '/bookmarks/:bookmarkId/delete/',
      name: 'delete-bookmark',
      component: DeleteSong
    },
    {
      path: '/songs/:songId/edit/',
      name: 'edit-song',
      component: EditSong
    },
    {
      path: '*',
      redirect: 'songs/'
    }
  ]
})
