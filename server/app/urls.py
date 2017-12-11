from django.urls import path
from .import views

urlpatterns = [
	path("status/", views.status_view, name="api-status"),
	path("register/", views.RegisterAPIView.as_view(), name="api-register"),
	path("login/", views.LoginAPIView.as_view(), name="api-login"),
]