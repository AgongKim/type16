from django.urls import path, include
from article import views

api_article_urls = [
    path('',views.ArticleAPI().as_view(http_method_names=['get', 'post']), name='list'),
    path('<int:article_id>/', views.ArticleDetailAPI.as_view(http_method_names=['get']), name='detail'),
    path('categories/', views.ArticleCategoriesAPI.as_view(http_method_names=['get']), name='categories'),
    path('like/', views.ArticleLikeAPI().as_view(http_method_names=['post']), name='like'),
]
urlpatterns = [
    path('api/v1/articles/', include(api_article_urls))
]
