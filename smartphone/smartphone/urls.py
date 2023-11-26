"""smartphone URL Configuration

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
from django.conf.urls import url
from owner import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',TemplateView.as_view(template_name='index.html')),
    url('showindex',views.showindex, name='showindex'),
    url('showcontact',views.showcontact,name='showcontact'),
    url('showlogin', views.showlogin, name='showlogin'),
    url('billing', views.showbilling, name='billing'),
    url('phones', views.showphones, name='phones'),
    url('payments', views.showpayments, name='payments'),
    url('smartphonedetails', views.smartphonedetails, name='smartphonedetails'),
    url('cuostmerdetails', views.cuostmerdetails, name='cuostmerdetails'),
    url('viewspd', views.viewspd, name='viewspd'),
    url('viewcuostmerdetails', views.viewcuostmerdetails, name='viewcuostmerdetails'),
    url('viewshopd', views.viewshopd, name='viewshopd'),
    url('viewcustd', views.viewcustd, name='viewcustd'),
    url('viewsaled', views.viewsaled, name='viewsaled'),
    url('viewbilling', views.viewbilling, name='viewbilling'),
    url('viewoffers', views.viewoffers, name='viewoffers'),

    url(r'^$',views.showindex, name='index'),
    url(r'^logcheck/$',views.logcheck, name='logcheck'),
    url(r'^insertowner$',views.insertowner, name='insertowner'),

    url('shop_details', views.shop_details, name='shop_details'),
    url('insert_mobile_details', views.insert_mobile_details, name='insert_mobile_details'),
    url('viewmobile_details', views.viewmobile_details, name='viewmobile_details'),
    url('viewshop_details', views.viewshop_details, name='viewshop_details'),
    url('customer_details', views.customer_details, name='customer_details'),
    url('viewcustomer_details', views.viewcustomer_details, name='viewcustomer_details'),
    url('sales_details', views.sales_details, name='sales_details'),
    url('viewsales_details', views.viewsales_details, name='viewsales_details'),
    url('offers', views.offers, name='offers'),
    url('viewoffers', views.viewoffers, name='viewoffers'),
    url('billing', views.billing, name='billing'),
    url('viewbilling', views.viewbilling, name='viewbilling'),
    url('finance', views.finance, name='finance'),
    url('viewfinance', views.viewfinance, name='viewfinance'),

]
