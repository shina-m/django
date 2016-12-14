from django.conf.urls import patterns, url

from addressbook import views

urlpatterns = patterns('',
   url(r'^view$', views.PersonList.as_view(), name='person_view'),
   url(r'^add$', views.PersonCreate.as_view(), name='person_add'),
   url(r'^edit/(?P<pk>\d+)$', views.PersonUpdate.as_view(), name='person_edit'),
   url(r'^delete/(?P<pk>\d+)$', views.PersonDelete.as_view(), name='person_delete'),
   )