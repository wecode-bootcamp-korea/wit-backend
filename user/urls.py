from django.urls import path
from .views import UserSignUpView, UserSignInView


urlpatterns = [
    path('/', UserSignUpView.as_view()),
    path('/login', UserSignInView.as_view())
    ]