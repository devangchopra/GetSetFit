"""django_fit URL Configuration

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
from django.urls import path, include
from fitme import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    # Fitmes
    path('', views.home, name='home'),
    path('create/', views.createfitme.as_view(), name='createfitme'),
    
    path('search/', views.image_view, name='search-in-ml'),

    path('success', views.success, name = 'success'), 

    path('current/', views.currentfitmes, name='currentfitmes'),
    path('completed/', views.completedfitmes, name='completedfitmes'),
    path('<int:fitme_pk>', views.viewfitme, name='viewfitme'),
    path('<int:fitme_pk>/complete', views.completefitme, name='completefitme'),
    path('<int:fitme_pk>/delete', views.deletefitme, name='deletefitme'),

]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)