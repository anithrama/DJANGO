"""
URL configuration for project2 project.

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
from django.urls import path
from app2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('add/',views.add_item,name='add'),
    path('list/',views.list,name='list'),
    path('forms/',views.user_form2,name='form'),
    path('edit/<int:p>',views.edit_item,name='edit'),
    path('delete/<int:p>',views.delete_item,name='delete'),
    path('form/',views.form3,name='form3'),
    path('new/',views.new,name='new'),

]
