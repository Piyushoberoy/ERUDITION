"""ERUDITION URL Configuration

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
from ERUDITION import views
from django.conf import settings
from django.conf.urls.static import static

#CHANGED DJANGO ADMIN PAGE TEXT
admin.site.site_header = "Erudition Administrator Panel"
admin.site.site_title = "Erudition Admin Portal"
admin.site.index_title = "Welcome to Erudition"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HOME, name='HOME'),
    path('signin', views.SIGNIN, name='SIGNIN'),
    path('signup', views.SIGNUP, name='SIGNUP'),
    path('signout', views.SIGNOUT, name='SIGNOUT'),
    path('forgot_password/', views.EMAIL_FOR_FORGOT_PASSWORD, name='FORGOT_PASSWORD'),
    path('verify', views.VERIFICATION, name='VERIFY'),
    path('reset_password', views.RESET_PASSWORD, name='RESET_PASSWORD'),
    # path('content/', views.CONTENT, name='CONTENT'),
    path('check/', include('CHECK.urls')),
    path('content/reading/', include('READING.urls')),
    path('content/video/', include('VIDEO.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)