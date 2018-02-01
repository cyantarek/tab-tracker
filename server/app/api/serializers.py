from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from .utils import create_token
from ..models import Song


class RegistrationSerializer(serializers.Serializer):
	email = serializers.EmailField(required=True, error_messages={"blank":"Don't you have an email?"})
	username = serializers.CharField(max_length=200, error_messages={"blank":"Give yourself a username"})
	password = serializers.CharField(max_length=200, label="Password", min_length=8, write_only=True,
									 style={'input_type': 'password'}, error_messages={
			"min_length":"Password required at least 8 characters",
			"blank": "Password field should not be blank and invalid",
			"invalid": "Provide a valid and strong password"
		})
	password2 = serializers.CharField(max_length=200, label="Confirm password", min_length=8, write_only=True,
									  style={'input_type': 'password'}, error_messages={
			"blank": "",
		},)

	def validate_password(self, value):
		data = self.get_initial()
		password = data.get("password")
		password2 = data.get("password2")

		if password != password2:
			raise ValidationError("Password didn't match")
		return value

	def validate_email(self, value):
		data = self.get_initial()
		email = data.get("email")
		object = User.objects.filter(email=email)
		if object:
			raise ValidationError("Email already in use")

		return value

	def validate_username(self, value):
		data = self.get_initial()
		username = data.get("username")
		obj = User.objects.filter(username=username)
		if obj:
			raise ValidationError("Username already exists")

		return value
# 	#
	def create(self, validated_data):
		username = validated_data["username"]
		email = validated_data["email"]
		password = validated_data["password"]
		user_obj = User.objects.create(username=username, email=email)
		user_obj.set_password(password)
		user_obj.save()

		return validated_data


class LoginSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	token = serializers.CharField(max_length=200, allow_blank=True, read_only=True)
	username = serializers.CharField(max_length=200, error_messages={"blank": "Enter your registered username"})
	password = serializers.CharField(max_length=200, label="Password", min_length=8, write_only=True,
									 style={'input_type': 'password'}, error_messages={
			"min_length": "Password required at least 8 characters",
			"blank": "Password field should not be blank and invalid",
			"invalid": "Provide a valid and strong password"
		})

# Deserialize
	def validate(self, data):
		username = data.get("username")
		password = data.get("password")

		user = User.objects.filter(username=username).first()
		if not user:
			raise ValidationError("User not registered", code=403)

		if not user.check_password(password):
			raise ValidationError("Password incorrect")

		token = create_token(user)

		data["token"] = token
		data["id"] = user.id
		return data


class UserSerializer(serializers.Serializer):
	id = serializers.IntegerField()
	email = serializers.EmailField()
	username = serializers.CharField(max_length=200)

class BookmarkSerializer(serializers.Serializer):
	id = serializers.IntegerField()
	user = serializers.CharField()
	song = serializers.CharField()

class SongSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	title = serializers.CharField(max_length=200)
	artist = serializers.CharField(max_length=200)
	genre = serializers.CharField(max_length=200)
	album = serializers.CharField(max_length=200)
	album_image = serializers.CharField(max_length=200)
	youtube_id = serializers.CharField(max_length=200)
	tab = serializers.CharField(allow_blank=True)
	lyrics = serializers.CharField(allow_blank=True)

	def create(self, validated_data):
		print("create called")
		song_obj = Song.objects.create(**validated_data)

		return validated_data

	def update(self, instance, validated_data):
		instance.title = validated_data.get("title")
		instance.artist = validated_data.get("artist")
		instance.genre = validated_data.get("genre")
		instance.album = validated_data.get("album")
		instance.album_image = validated_data.get("album_image")
		instance.youtube_id = validated_data.get("youtube_id")
		instance.tab = validated_data.get("tab")
		instance.lyrics = validated_data.get("lyrics")
		instance.save()
		print("update called")

		return instance

