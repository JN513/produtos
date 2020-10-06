"""produtos URL Configuration

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
from core import urls
from django.contrib.auth import views

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    #auth views
    path('auth/password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('auth/password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('auth/password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('auth/password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('auth/reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('auth/reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


