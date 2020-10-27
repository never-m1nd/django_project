from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index_url'),
    path('create/', CreatePost.as_view(), name='create_post_url'),
    path('post/<int:pk>-<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<int:pk>-<str:slug>/update/', UpdatePost.as_view(), name='post_update_url'),
    path('post/<int:pk>-<str:slug>/delete/', DeletePost.as_view(), name='post_delete_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    ]
