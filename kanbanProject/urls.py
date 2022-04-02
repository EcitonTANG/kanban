"""kanbanProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from kanban.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('executor', Executor_TabAPIView.as_view()),
    path('card', Card_TabAPIView.as_view()),
    path('column', Column_TabAPIView.as_view()),
    path('executor/<int:pk>', Executor_TabAPIView.as_view()),
    path('column/<int:pk>', Column_TabAPIView.as_view()),
    path('card/<int:pk>', Card_TabAPIView.as_view()),
]
