"""FinalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from details import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home , name='home' ),
    path('result/' , views.myres , name='result'),
    path('ranks/' , views.myrank , name='ranks'),
    path('contact/' , views.contactpage , name='contact'),
    path('postContact/' , views.ContactAPI.as_view() , name='postcontact'),
    path('createpdf/', views.createpdf, name='createpdf'),
    path('resultapi/' , views.AllResultsApi.as_view() , name='ResultApi'),
    path('studentapi/' , views.AllStudentsApi.as_view() , name='StudentApi')
]

admin.site.index_title = 'Entry Results and Details'
admin.site.site_header = "CSE,SUST"
admin.site.site_title= "Admin"
