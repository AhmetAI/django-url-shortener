from . import views
from django.urls import path

urlpatterns = [
    path('', views.indexView, name="index"),
    path('<str:short_url_slug>/', views.shorten_url, name='short_url'),
]
