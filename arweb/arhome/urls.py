from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.Home, name='home'),
    url(r'api/$', views.MemberList.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.MemberDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
