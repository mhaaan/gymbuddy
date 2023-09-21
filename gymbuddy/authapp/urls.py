from django.urls import path
from authapp import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('signup', views.signup, name='signup')   ,
    path('login', views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout')
]

# hi