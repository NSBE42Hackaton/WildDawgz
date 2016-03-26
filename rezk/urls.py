"""rezk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   url(r'^$', 'reg.views.home', name='home'),
   url(r'^start', 'reg.views.start', name='start'), 
   url(r'^results', 'give.views.show_request', name='results'),
   url(r'^makerequest/', 'request.views.submit_request', name='request'),
   url(r'^(?P<id>\d+)/$', 'give.views.detail', name='detail'), 
   url(r'^admin/', admin.site.urls),
   url(r'^accounts/', include('registration.backends.simple.urls')),

]
