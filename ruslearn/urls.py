"""ruslearn URL Configuration

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
from main_app import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('logout', views.logout_request, name='logout'),
    path('accounts/login/', views.login_request, name='login'),
    path('add_pack', views.create_pack, name='add_pack'),
    path('delete_pack', views.delete_pack, name='delete_pack'),
    path('add_card', views.add_card, name='add_card'),
    path('delete_card', views.delete_card, name='delete_card'),
    path('view_card', views.view_card, name='view_card'),
    path('next_card', views.get_next_card, name='next_card'),
    path('subscriptions', views.subscription_page, name='subscriptions')
]
