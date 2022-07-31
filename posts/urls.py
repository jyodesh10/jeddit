from django.urls import path
from posts import views

urlpatterns = [
    path('api/posts', views.PostList.as_view()),
    path('api/posts/<int:pk>/vote', views.VoteCreate.as_view())
]
