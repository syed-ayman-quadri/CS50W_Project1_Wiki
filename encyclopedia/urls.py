from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:title>', views.entry, name='entry'),
    path('search/', views.search, name='search'),
    path('createpage/', views.createpage, name='createpage'),
    path('edit/', views.edit, name='edit'),
    path('saved/', views.saved, name='saved'),
    path('randomom', views.randomom, name='randomom')
]
