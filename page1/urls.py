from django.urls import path 
from . import views 



urlpatterns = [
    path('', views.store_data, name='page1'),
]