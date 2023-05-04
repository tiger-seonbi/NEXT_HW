from django.urls import path
from Blog import views

#url name 스페이스
app_name = 'Blog'

#
urlpatterns = [
    path('', views.home, name="home"),
    path('new/', views.new, name="new"),
    path('detail/<int:post_id>/', views.detail, name="detail"),
    path('update/<int:post_id>/', views.update, name="update"),
    path('delete/<int:post_id>/', views.delete, name="delete"),
]
