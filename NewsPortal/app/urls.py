from django.urls import path
from django.views.decorators.cache import cache_page

from .views import PostList, PostCreate, PostDetail, PostDelete, PostUpdate, ResponseList, response

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
    path('<int:pk>/update', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/response', response, name='response'),
    path('response/', ResponseList.as_view(), name='response_list')
]