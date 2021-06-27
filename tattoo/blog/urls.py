from django.urls import path

from . import views


urlpatterns = [
    path('tags/', views.TagViewSet.as_view({'get': 'list'})),
    path('tag/<int:pk>', views.TagViewSet.as_view({'get': 'retrieve'})),

    path('posts/', views.PostViewSet.as_view({'get': 'list'})),
    path('post/<str:slug>', views.PostViewSet.as_view({'get': 'retrieve'})),
]
