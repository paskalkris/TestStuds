from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.GroupsView.as_view(), name='groups_list'),
]