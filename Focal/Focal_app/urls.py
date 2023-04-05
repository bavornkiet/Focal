from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('Activities/<int:activity_id>', views.activity_by_id, name='activity_by_id')
]