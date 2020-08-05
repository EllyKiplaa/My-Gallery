from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns=[
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.gallery, name='gallery'),
    url(r'^search/', views.search_results, name = 'search_results'),
    url(r'location/(\d+)',views.filter_by_location,name='location'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 