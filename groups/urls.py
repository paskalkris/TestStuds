from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.GroupsView.as_view(), name='groups_list'),
    url(r'^$', views.groups_list, name='groups_list'),
    url(r'^(?P<group_id>[0-9]+)/$', views.studs_list, name='studs_list'),
    url(r'^create/$', views.group_create, name='group_create'),
    url(r'^(?P<group_id>[0-9]+)/edit/$', views.group_edit, name='group_edit'),
    url(r'^(?P<group_id>[0-9]+)/delete/$', views.group_delete, name='group_delete'),
    url(r'^(?P<group_id>[0-9]+)/confirm_delete/$', views.confirm_delete, name='confirm_delete'),
]
