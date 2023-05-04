from django.urls import path
from accounts import views

#url name 스페이스
app_name = 'accounts'

#
urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
]
