from django.urls import path
from .import views as views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
	path("status/", views.status_view, name="api-status"),
	path("login/", views.LoginAPIView.as_view(), name="api-login"),
	path("logout/<user>/", views.logout_view, name="api-logout"),
	path("register/", views.RegisterAPIView.as_view(), name="api-register"),
	path("users/", views.UserListAPIView.as_view(), name="api-user-list"),
	path("get_token/", obtain_jwt_token, name="api-user-list"),


	path("songs/", views.SongAPIView.as_view(), name="api-songs-list"),
	path("bookmarks", views.BookmarksAPIView.as_view(), name="api-bookmarks"),
	path("bookmarks/add/", views.BookmarksAPIView.as_view(), name="api-add-bookmark"),
	path("bookmarks/delete/", views.BookmarksAPIView.as_view(), name="api-delete-bookmark"),
	path("songs/<songId>/", views.SongAPIView.as_view(), name="api-songs-detail"),
	path("songs/delete/<songId>/", views.SongAPIView.as_view(), name="api-songs-delete"),
	path("songs/update/<songId>/", views.SongAPIView.as_view(), name="api-song-update"),
]