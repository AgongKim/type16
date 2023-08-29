from django.urls import path, include
from . import views

api_comment_urls = [
    path('',views.CommentAPI().as_view(), name='list'),
    path('like/', views.CommentLikeAPI().as_view(http_method_names=['post']), name='like'),
]
urlpatterns = [
    path('api/v1/comments/', include(api_comment_urls))
]
