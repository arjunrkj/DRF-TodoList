from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.apioverview,name='api-overview'),
    path('task-list/', views.tasklist,name='task-list'),
    path('detail-view/<str:pk>/', views.detailview,name='detail-view'),
    path('task-create/', views.create,name='task-create'),
    path('task-update/<str:pk>/', views.update,name='task-update'),
    path('task-delete/<str:pk>/', views.delete,name='task-delete'),
]