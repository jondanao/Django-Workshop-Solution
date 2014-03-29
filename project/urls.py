from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^(?P<category_slug>[-\w]+)/$', views.category), 
    url(r'^(?P<category_slug>[-\w]+)/(?P<article_id>\d+)/([-\w]+)/$', views.article),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
