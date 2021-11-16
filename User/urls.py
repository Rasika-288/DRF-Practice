from django.urls import path
from .views import UserApi, LoginApi, SignUpApi

urlpatterns = [
    path('', UserApi.as_view()),
    path('signup/',SignUpApi.as_view()),
    path('login', LoginApi.as_view()),
]
