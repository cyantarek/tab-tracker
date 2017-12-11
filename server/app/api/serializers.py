from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from django.db.models import Q


class RegistrationSerializer(serializers.ModelSerializer):
	password = serializers.CharField(max_length=200, label="Password", min_length=8, write_only=True, style={'input_type': 'password'})
	password2 = serializers.CharField(max_length=200, label="Confirm password", min_length=8, write_only=True, style={'input_type': 'password'})
	email = serializers.EmailField(required=True)
	class Meta:
		model = User
		fields = [
			"username",
			"email",
			"password",
			"password2",

		]


	def validate_password(self, value):
		data = self.get_initial()
		password = data.get("password")
		password2 = data.get("password2")

		if password != password2:
			raise ValidationError("Password didn't match")
		return value

	def create(self, validated_data):
		username = validated_data["username"]
		email = validated_data["email"]
		password = validated_data["password"]
		user_obj = User(
			username=username,
			email=email,
		)
		user_obj.set_password(password)
		user_obj.save()

		return validated_data


class LoginSerializer(serializers.ModelSerializer):
	token = serializers.CharField(max_length=200, read_only=True)
	class Meta:
		model = User
		fields = [
			"username",
			"password",
			"token",

		]

	def validate(self, data):
		username = data.get("username")
		password = data.get("password")
		if not username or not password:
			raise ValidationError("Username and Password is required to login")

		user = User.objects.filter(
			Q(username=username) & Q(password=password)
		).distinct()

		if user.exists() and user.count() == 1:
			user = user.first()

		else:
			raise ValidationError("Username and/or password error")

		return data
