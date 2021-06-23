from django.urls import path

from .views import index, graduate_view

urlpatterns = [
    path('', index, name='index'),
    path('graduates/<int:id>/', graduate_view, name='graduate_view'),
]
