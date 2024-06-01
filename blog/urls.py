from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogDeleteView, BlogUpdateView

app_name = BlogConfig.name

urlpatterns = [
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_detail/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('create_blog/', BlogCreateView.as_view(), name='create_blog'),
    path('delete_blog/<int:pk>', BlogDeleteView.as_view(), name='delete_blog'),
    path('update_blog/<int:pk>', BlogUpdateView.as_view(), name='update_blog'),
]
