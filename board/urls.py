from django.urls import path
from .views import content, PostList, sign_me, PostDetail, PostCreate, PostUpdate, PostDelete, ResponseCreate, ResponseList, ResponseDelete, ResponseDetail, AllResponseList, personal_page
from django.views.decorators.cache import cache_page

urlpatterns = [
   path('', content),
   path('personal_page/', personal_page),
   path('posts/', PostList.as_view()),
   path('posts/sign_me/', sign_me, name='sign_me'),
   path('posts/<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('posts/create/', PostCreate.as_view(), name='post_create'),
   path('posts/all_responses/', AllResponseList.as_view(), name='response_list'),
   path('posts/all_responses/<int:pk>', ResponseDetail.as_view(), name='response_detail'),
   path('posts/all_responses/<int:pk>/delete/', ResponseDelete.as_view(), name='delete_response'),
   path('posts/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('posts/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('posts/<int:pk>/response/', ResponseCreate.as_view(), name='post_response'),
   path('posts/<int:pk>/all_responses/', ResponseList.as_view(), name='all_responses'),
]