"""house_rental URL Configuration

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
from django.conf.urls import url,include
from temp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('fedback_owner/', include('fedback_owner.url')),
    url('login/',include('login.url')),
    url('maintanance_trquest/',include('maintanance_request.url')),
    url('notification/',include('notification.url')),
    url('owner/',include('owner.url')),
    url('pay_rent/',include('pay_rent.url')),
    url('pay_security/',include('pay_security.url')),
    url('property/',include('property.url')),
    url('property_request/',include('property_request.url')),
    url('rent_payment/',include('rent_payment.url')),
    url('security_payment/',include('security_payment.url')),
    url('tenant/',include('tenant.url')),
    url('type/',include('type.url')),
    url('temp/', include('temp.url')),
    url('$',views.home)
]
