from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from user.views import RegisterAPIView, AuthAPIView

urlpatterns = [
    path("", AuthAPIView.as_view()),
    path("register/", RegisterAPIView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
]