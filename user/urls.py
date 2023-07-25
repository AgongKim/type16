from django.urls import path, include
from user import views

api_user_urls = [
    path('',views.UserAPI.as_view(http_method_names=['get', 'post', 'patch', 'delete']), name='list'),
]

urlpatterns = [
    path('api/v1/users/', include(api_user_urls))
]