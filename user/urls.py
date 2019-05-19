from django.urls import path
from .views import UserSignUpView, UserSignInView, UserDetailView


urlpatterns = [
    path('/', UserSignUpView.as_view()),
    path('/signin', UserSignInView.as_view()),
    path('/detail', UserDetailView.as_view())
    ]