from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/(?P<group_id>[0-9]+)/$', views.stud_create, name='stud_create'),
    url(r'^(?P<stud_id>[0-9]+)/edit/(?P<group_id>[0-9]+)/$', views.stud_edit, name='stud_edit'),
    url(r'^(?P<stud_id>[0-9]+)/delete/(?P<group_id>[0-9]+)/$', views.stud_delete, name='stud_delete'),
]