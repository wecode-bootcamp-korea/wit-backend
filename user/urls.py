from django.urls import path
from .views import UserView, UserSignInView


urlpatterns = [
    path('/signup', UserSignUpView.as_view()),
    path('/signin', UserSignInView.as_view())
    ]