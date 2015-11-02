from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<group_pk>[0-9]+)/$', views.StudsView.as_view(), name='studs_list'),
]