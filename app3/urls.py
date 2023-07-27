from django.urls import path
from app3.views import *
app_name='fun'
urlpatterns=[
    path('fun/',fun,name='fun'),
]