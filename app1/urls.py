from django.urls import path
from app1.views  import *
app_name='something'
urlpatterns=[
    path('file1/',file1,name='file1'),
    path('file2/',file2,name='file2'),
    path('file3/',file3,name='file3'),
]