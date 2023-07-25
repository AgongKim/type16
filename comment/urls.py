from django.urls import path, include
from . import views

api_comment_urls = [
    path('',views.CommentAPI().as_view(http_method_names=['get', 'post']), name='list'),
    path('like/', views.CommentAPI().as_view(http_method_names=['post']), name='like'),
]
urlpatterns = [
    path('api/v1/comments/', include(api_comment_urls))
]
