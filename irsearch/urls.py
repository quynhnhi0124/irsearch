from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ketqua/', views.index_result, name = "result"),
]