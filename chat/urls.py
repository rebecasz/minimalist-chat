from django.urls import path
from . import views


urlpatterns=[
    path('', views.home,name="home"),
    path('<str:room>/', views.room,name="room"),
    path('checkview',views.checkview, name="checkview"),
    path('send', views.send, name="send"),
    path('getMessages/<str:room>/',views.getMesseges, name="getMesseges"),
    path('/', views.login_view, name="login"),
    path('', views.logout_view, name="logout"),
    path('accounts/sign_up/',views.sign_up,name="sign-up")
]