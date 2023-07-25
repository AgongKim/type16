from django.urls import path

from .views import detail

urlpatterns = [
    path("mtype/<str:mbti>/", detail, name="mtype-detail"),
]