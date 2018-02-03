from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from arhome import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', include('arhome.urls')),
    url(r'^$', views.Home.as_view()),
    url(r'^about/$', views.About.as_view()),
    url(r'^events/$', views.Events.as_view()),
    url(r'^wip/$', views.Wip.as_view()),
    url(r'^api-auth/$', include('rest_framework.urls', namespace='rest_framework'))
]

print(settings.DEBUG)
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

