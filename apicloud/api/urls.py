from django.urls import path
from .views import PostAPIView, PostDetailAPIView

app_name = 'api'

urlpatterns = [
    path('v1/post/', PostAPIView.as_view(), name='post-list'),
    path('v1/post/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
]
