from django.urls import path

from .views import index,about,contact,team,detail
urlpatterns=[
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('team/',team,name='team'),
    path('detail/',detail,name='detail'),
]