"""services URL Configuration

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
from rest_framework.urlpatterns import format_suffix_patterns
from apis import views

admin.site.site_title = 'S. M. Autade'
admin.site.site_header = 'Autade Groups'
# admin.site.index_title = 'S. M. Autade'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logins/', views.loginList.as_view()),
    path('villages/', views.villageList.as_view()),
    # path('villages/<id>/', views.villageEdit.as_view()),
    path('taluka/', views.talukaList.as_view()),
    path('visits/', views.visitHistoryList.as_view()),
]
