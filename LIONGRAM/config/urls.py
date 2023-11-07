"""config URL Configuration

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
from django.urls import path, include
from posts.views import index, url_view, url_parameter_view, funtion_view, class_view, post_list_view, post_detail_view, post_create_view, post_update_view, post_delete_view 

urlpatterns = [
    path("admin/", admin.site.urls),
    path('url/', url_view),
    path('url/<str:username>/', url_parameter_view), #경로로 받기
    path('fbv/', funtion_view),
    path('cbv/', class_view.as_view()),
    path('',index, name='index'),
    path('posts/', include('posts.urls', namespace='posts')),
]
