from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^api/$', views.APIList.as_view(), name='api-list'),
    url(r'^api/(?P<pk>[0-9]+)/$', views.APIDetail.as_view(), name='api-detail'),
]