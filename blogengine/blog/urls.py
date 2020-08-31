from django.urls import path
from .views import *

urlpatterns = [
    path('', redirect_to_index),
    path('blog/', Index.as_view(), name='index_url'),
    path('create/', CreatePost.as_view(), name='create_post_url'),
    path('blog/post/<int:pk>-<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('blog/post/<int:pk>-<str:slug>/update/', UpdatePost.as_view(), name='post_update_url'),
    path('blog/tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    ]
