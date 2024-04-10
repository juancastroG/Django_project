from django.urls import path

from Accesorios import admin, views


urlpatterns = [
    path('', views.AccesorioView.as_view(), name='accesorio_list'),
]
