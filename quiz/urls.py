#여기서 생성하고 myapi에 있는 url로 연결

from django.urls import path, include
from .views import helloAPI, randomQuiz

urlpatterns = [
    path("hello/", helloAPI),
    path("<int:id>/", randomQuiz),
]