from django.urls import path
from blog.views import PostsByCategory, PostsList, PostDetail

app_name = 'blog'

urlpatterns = [
    path('', PostsList.as_view(), name='blog'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('category/<slug:slug>/', PostsByCategory.as_view(), name='category'),
] 