from django.urls import path
from . import views

urlpatterns = [
    path('',views.reg,name='reg'),
    path('sea/',views.sea,name='sea'),
    path('live/',views.live,name='live'),
    path('many/',views.many,name='many'),
]