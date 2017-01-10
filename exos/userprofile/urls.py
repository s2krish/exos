from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add/$', views.UserProfileCreateView.as_view(), name='add'),
    url(r'^list/$', views.UserProfileListView.as_view(), name='list'),
    url(r'^update/(?P<pk>\w+)/$', views.UserProfileUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\w+)/$', views.UserProfileDeleteView.as_view(), name='delete'),
]
