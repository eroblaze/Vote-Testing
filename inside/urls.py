from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('display/', views.display, name='display'),
    path('vote/', views.vote, name="vote"),
]