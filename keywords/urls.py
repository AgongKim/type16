from django.urls import path, include
from . import views

api_keyword_urls = [
    path('', views.KeywordCreateAPI.as_view(), name='list'),
]

urlpatterns = [
    path('api/v1/keywords/', include(api_keyword_urls))
]
