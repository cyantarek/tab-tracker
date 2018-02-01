from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from .models import Song, Bookmark
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .api.serializers import RegistrationSerializer, LoginSerializer, UserSerializer, SongSerializer, BookmarkSerializer
from rest_framework.authtoken.models import Token
from django.contrib.postgres.search import SearchVector


def status_view():
	stat = {
		"message": "status OK!"
	}
	return JsonResponse(stat)


class RegisterAPIView(APIView):
	serializer_class = RegistrationSerializer
	permission_classes = [AllowAny]

	def post(self, reqeust):
		data = reqeust.data
		serializer = RegistrationSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class LoginAPIView(APIView):
	serializer_class = LoginSerializer
	permission_classes = [AllowAny]

	def post(self, request):
		data = request.data
		serializer = LoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			print(serializer.data)
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def logout_view(request, user):
	user = User.objects.get(username=user)
	token = Token.objects.get(user_id=user.id)
	token.delete()
	return HttpResponse("Logout successfully")


class UserListAPIView(APIView):
	serializer_class = UserSerializer

	permission_classes = [AllowAny]

	def get(self, request):
		users = User.objects.all()
		serialize = UserSerializer(users, many=True)
		return Response(serialize.data, status=status.HTTP_200_OK)


class SongAPIView(APIView):
	permission_classes = [AllowAny]
	serializer_class = SongSerializer

	def get(self, request, songId=None):
		if songId:
			try:
				song = Song.objects.get(id=songId)
				serializer = SongSerializer(song)
				return Response(serializer.data, status=status.HTTP_200_OK)
			except:
				return Response({"message": "Song not found, sorry"}, status=status.HTTP_400_BAD_REQUEST)

		query = request.GET.get("search")
		if not query or query == "undefined":
			songs = Song.objects.all()
			if songs:
				serialize = SongSerializer(songs, many=True)
				return Response(serialize.data, status=status.HTTP_200_OK)
		else:
			songs = Song.objects.annotate(
				search=SearchVector("title", "album", "artist", "genre"),
			).filter(search=query)
			serialize = SongSerializer(songs, many=True)
			return Response(serialize.data, status=status.HTTP_200_OK)

	# songs = Song.objects.all()
	# if songs:
	# 	serialize = SongSerializer(songs, many=True)
	# 	return Response(serialize.data, status=status.HTTP_200_OK)
	# return Response({"message": "An error occured trying to fetch the songs. Maybe no song exists"},
	# 				status=status.HTTP_404_NOT_FOUND)

	def post(self, request):
		data = request.data
		serializer = SongSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, songId):
		data = request.data
		try:
			song = Song.objects.get(id=songId)
			serializer = SongSerializer(song, data=data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_200_OK)
		except:
			return Response({"message": "Song not found, sorry"}, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, songId):
		try:
			song = Song.objects.get(id=songId)
			song.delete()
			return Response({"message": "Song deleted successfully"}, status=status.HTTP_200_OK)
		except:
			return Response({"message": "Song not found, sorry"}, status=status.HTTP_400_BAD_REQUEST)


class BookmarksAPIView(APIView):
	serializer_class = BookmarkSerializer
	permission_classes = [AllowAny]

	def get(self, request):
		query_song = request.GET.get("songId")
		query_user = request.GET.get("userId")
		if query_song and query_user:
			bookmarks = Bookmark.objects.get(song=query_song, user=query_user)
			if bookmarks:
				serializer = BookmarkSerializer(bookmarks)
				return Response(serializer.data, status=status.HTTP_200_OK)
		elif query_user:
			bookmarks = Bookmark.objects.filter(user=query_user)
			if bookmarks:
				serializer = BookmarkSerializer(bookmarks, many=True)
				return Response(serializer.data, status=status.HTTP_200_OK)
		return Response({"message": "No bookmark found for your query"}, status=status.HTTP_400_BAD_REQUEST)

	def post(self, request):
		query_song = request.data["songId"]
		song = Song.objects.get(id=query_song)
		query_user = request.data["userId"]
		user = User.objects.get(id=query_user)
		if song and user:
			bookmark = Bookmark.objects.filter(user=user, song=song)
			if bookmark:
				return Response({"message": "Bookmark already exists"}, status=status.HTTP_400_BAD_REQUEST)
			bookmark = Bookmark(user=user, song=song)
			bookmark.save()
			if bookmark:
				serializer = BookmarkSerializer(bookmark)
				return Response(serializer.data, status=status.HTTP_200_OK)
		return Response({"message": "No bookmark found for your query"}, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request):
		bookmark_id = request.data["id"]
		bookmark = Bookmark.objects.get(id=bookmark_id)
		if bookmark:
			bookmark.delete()
			return Response({"message": "Bookmark deleted"}, status=status.HTTP_200_OK)
		return Response({"message": "No bookmark found for your query"}, status=status.HTTP_400_BAD_REQUEST)
