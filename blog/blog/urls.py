"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import myapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.home,name="home"),
    path('wordcount/', myapp.views.wordcount,name="wordcount"),
    path('wordcount/about/', myapp.views.wordcountAbout,name="wordcountAbout"),
    path('wordcount/result/', myapp.views.wordcountResult,name="wordcountResult"),
    path('queryset/', myapp.views.queryset,name="queryset"),
    path('detail/<int:blog_id>', myapp.views.detail, name="detail"),
    path('service/',myapp.views.service, name="service"),
    path('guest/', myapp.views.guest,name="guest"),
    path('guest/write',myapp.views.guestWrite,name="guestWrite"),
    path('guest/result/<int:guest_id>',myapp.views.guestResult,name="guestResult"),
    path('guest/create', myapp.views.guestCreate,name="guestCreate"),
    path('gallery/', myapp.views.gallery, name="gallery"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
