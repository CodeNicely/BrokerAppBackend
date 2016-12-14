"""BrokerApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from splash_screen.views import splash_scr_response
from otp.views import send_otp
from otp.views import verify_otp
from register_deals.views import register_offer,send_offers 
from final_deals.views import final_deals_to_show,final_deals_to_get
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^splash_screen/', splash_scr_response),
    url(r'^send_otp/', send_otp),
    url(r'^verify_otp/', verify_otp),
    url(r'^register_deals/', register_offer ),
    url(r'^send_deals/',send_offers),
    url(r'^get_final_deals/',final_deals_to_show),
    url(r'^store_final_deals/',final_deals_to_get),
]
