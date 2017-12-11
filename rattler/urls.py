"""rattler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import handler404
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # Login View
    path(
        'login/', 
        auth_views.LoginView.as_view(redirect_authenticated_user=True), 
        name='login'
    ),
    # Logout View
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='/'),
        name='logout'
    ),

    # Password Views
    path(
        'password/',
        include('apps.password.urls'),
        name='password'
    ),

    path('register/', include('apps.register.urls'), name='register'),
    # Django Admin
    path('djangoAdmin/', admin.site.urls),
    # Global Routes
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/test/', views.registerTest, name='registerTest'),
    path('community/', views.community, name='community'),
    path('profile/me/', views.profileMe, name='profileMe'),
    path('admin/', views.admin, name='admin'),
    path('settings/', views.settings, name='settings'),
    path('help/', views.help, name='help'),
    path('', include('apps.index.urls'), name='index'),
]

# Error Handlers
handler404 = 'rattler.views.handler404'
