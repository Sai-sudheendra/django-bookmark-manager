from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookmark_list, name='bookmark_list'),
    path('add/', views.bookmark_create, name='bookmark_add'),
    path('edit/<int:pk>/', views.bookmark_update, name='bookmark_edit'),
    path('delete/<int:pk>/', views.bookmark_delete, name='bookmark_delete'),
]
