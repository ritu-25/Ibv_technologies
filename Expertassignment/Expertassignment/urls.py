"""
URL configuration for Expertassignment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from myApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home, name='home'),
    path('base/',views.base,name='base'),
    path('gauranteedMarks/',views.gauranteedmarks),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'), 
    path('whyus/',views.whyus),
    path('order/',views.order, name='order'),
    path('success/',views.success,name='success'),
    path('about/',views.about),
    path('result/',views.result),
    path('megaoffer/',views.megaoffer),
    path('list/',views.list_result),
    path('send-email/', views.send_email, name='send_email'),
    path('email-success/', views.success_email, name='success_email'),
    

    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
 