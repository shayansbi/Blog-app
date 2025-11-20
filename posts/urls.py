from django.urls import path

from .views import (PostListView, PostDetailView,
                    PostDeleteView, PostUpdateView, PostCreateView)


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('new/', PostCreateView.as_view(), name='post_new')
]