"""
URL configuration for projectMix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from appMix import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('mix/', views.mix, name='mix'),
    path('err/', views.err, name='err'),
    path('detail/<int:item_id>', views.detail, name='detail'),
    path('update/<int:item_id>', views.update, name='update'),
    path('delete/<int:item_id>', views.delete, name='delete'),
    path('delete-comment/<int:item_id>/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('recomment/<int:item_id>/<int:comment_id>', views.recomment, name='recomment'),
    path('delete-recomment/<int:item_id>/<int:comment_id>/<int:recomment_id>', views.recomment_delete, name='recomment_delete'),
    path('registration/signup/', views.signup, name="signup"),
    path('registration/login/', views.login, name="login"),
    path('registration/logout/', views.logout, name="logout"),
    path('accounts/', include('allauth.urls')),
]
