"""dualrobot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from dualapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('torvaldsForward/', views.torvaldsForward),
    path('torvaldsBackward/', views.torvaldsBackward),
    path('torvaldsLeft/', views.torvaldsLeft),
    path('torvaldsRight/', views.torvaldsRight),
    path('stop/', views.stop),
    path('directionone/', views.directionone),
    path('directiontwo/', views.directiontwo),
    path('directionthree/', views.directionthree),
    path('directionfour/', views.directionfour),
    path('stoptwo/', views.stoptwo),
    path('eyeon/', views.eyeon),
    path('eyeoff/', views.eyeoff),
    path('torvaldson/', views.torvaldson),
    path('torvaldsoff/', views.torvaldsoff),
    path('minus90/', views.minus90),
    path('minus45/', views.minus45),
    path('zero/', views.zero),
    path('positive45/', views.positive452),
    path('positive90/', views.positive902),
    path('minus902/', views.minus902),
    path('minus452/', views.minus452),
    path('zero2/', views.zero),
    path('positive452/', views.positive452),
    path('positive902/', views.positive902),
    path('pwmThirty/', views.pwmThirty),
    path('pwmFifty/', views.pwmFifty),
    path('pwmFull/', views.pwmFull),
    path('pwmThirty2/', views.pwmThirty2),
    path('pwmFifty2/', views.pwmFifty2),
    path('pwmFull2/', views.pwmFull2),
    
    
]
