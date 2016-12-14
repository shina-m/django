"""spcrud URL Configuration

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


from addressbook import views

urlpatterns = [
    url(r'^$', views.PersonIndex.as_view()),
    url(r'^admin/', admin.site.urls),
   # url(r'^view/$','spcrud.addressbook.views.list')
    url(r'^view$', views.PersonList.as_view(), name='person_list'),
    url(r'^add$', views.PersonCreate.as_view(), name='person_add'),
    url(r'^edit/(?P<pk>\d+)$', views.PersonUpdate.as_view(), name='person_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.PersonDelete.as_view(), name='person_delete'),
]
