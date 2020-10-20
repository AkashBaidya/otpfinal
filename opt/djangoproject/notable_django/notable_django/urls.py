"""notable_django URL Configuration

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
from api.resources import NoteResource
from api.resources import RegistrationResource
from api.resources import CheckPhoneNumberResource
from api.resources import CheckPasscodeResource
from api.resources import EnterRegistrationData
from api.resources import OtpGenerationResource
from api.resources import OtpVerifyResource
from api.resources import ShopResource


registration_resource=RegistrationResource()

phone_resource= CheckPhoneNumberResource();

note_resource = NoteResource()

otp_resource=OtpGenerationResource()

passcode_resource=CheckPasscodeResource();

enterdata_resource=EnterRegistrationData()

otp_verify_resource=OtpVerifyResource()

shop_resource=ShopResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(note_resource.urls)),
    url(r'^api/', include(phone_resource.urls)),
    url(r'^api/', include(registration_resource.urls)),
    url(r'^api/', include(passcode_resource.urls)),
    url(r'^api/', include(enterdata_resource.urls)),
    url(r'^api/', include(otp_resource.urls)),
    url(r'^api/', include(otp_verify_resource.urls)),
    url(r'^api/', include(shop_resource.urls)),
]

