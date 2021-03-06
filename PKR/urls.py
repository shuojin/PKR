"""PKR URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
import pkr_user.views as user_views

urlpatterns = [
    url(r'^$', user_views.home, name = 'home'),
    url(r'^user/', include('pkr_user.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/', user_views.user_logout, name="logout"),
    url(r'^dashboard/', user_views.dashboard, name = 'dashboard'),
    url(r'^items/', user_views.items, name='item'),
    url(r'^request_items/', user_views.items_request, name='item_request'),
    url(r'^add_product', user_views.add_product, name= 'add_product'),
    url(r'^update_stock', user_views.update_stock, name = 'update_stock'),
]
