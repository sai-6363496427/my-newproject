from firstapp import views
from django.urls import path


urlpatterns = [
    path('',views.registrstion,name='register'),
    path('home/',views.home,name='home'),
    path('login/',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('user_profile/',views.user_profile,name='user_profile'),
 ]


