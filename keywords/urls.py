from django.urls import path, include
from . import views

api_keyword_urls = [
    path('create/', views.KeywordCreateAPI.as_view(), name='keyword_create'),
]

urlpatterns = [
    path('api/v1/keywords/', include(api_keyword_urls))
]
