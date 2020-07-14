"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIndex,name='main'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('login_check/',views.login_check,name='login_check'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
    path('schedule_course/',views.schedule_course,name='schedule_course'),
    path('save_course/',views.save_course,name='save_course'),
    path('view_course/',views.view_course,name='view_course'),
    path('update_course/',views.update_course,name='update_course'),
    path('update/',views.update,name='update'),
    path('delete_record/',views.delete_record,name='delete_record'),
    path('view_online_course/',views.view_online_course,name='view_online_course'),
    path('stu_register/',views.stu_register,name='stu_register'),
    path('save_student/',views.save_student,name='save_student'),
    path('stu_login/',views.stu_login,name='stu_login'),
    path('stu_validate/',views.stu_validate,name='stu_validate')
]
