"""blogProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/', views.new, name='new'),
    path('home/', views.home, name='home'),
    path('detail/<int:article_id>/', views.detail, name='detail'),
    path('detail/<int:article_id>,<int:comment_pk>/', views.comment_delete, name='comment_delete'),
    path('detail/<int:article_id>,<int:comment_pk>/reply', views.reply, name='reply'),
    path('detail/<int:article_id>,<int:comment_pk>/reply/<int:reply_pk>', views.reply_delete, name='reply_delete'),
    path('board/<str:board_name>/',views.board, name="board"),
]
