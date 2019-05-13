from django.urls import path
from .views import TrainInfoView, TrainResultView


urlpatterns = [
    path('/all', TrainInfoView.as_view()),
    path('', TrainResultView.as_view())
    ]