from django.urls import path

from .views import index, about, contact, team, detail, login_view, logout_view

urlpatterns=[
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('team/',team,name='team'),
    path('detail/',detail,name='detail'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
]