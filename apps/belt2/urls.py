from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.dashboard, name="dashboard"),
    url(r'^dashboard$', views.dashboard, name="dashboard"),
    url(r'^add_item$', views.add_item, name="add_item"),
    url(r'^create$', views.create, name="create"),
    url(r'^(?P<id>\d+)/showmitem$', views.showitem, name="showitem"),
    url(r'^add_like$', views.add_like, name="add_like"),
    url(r'^remove_like$', views.remove_like, name="remove_like"),
    url(r'^delete_item/(?P<id>\d+)$', views.delete_item, name="delete_item"),
    url(r'^logout$', views.logout, name="logout"),
]
