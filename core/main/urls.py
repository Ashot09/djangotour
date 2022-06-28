from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='index'),
    path('aboutus/', views.AboutListView.as_view(), name = 'aboutus'),
    path('stays/', views.StaysListView.as_view(), name = 'stays')
]
