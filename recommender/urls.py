from django.conf.urls import patterns, include, url
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from recommender.views import index

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'recommender.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^names/', include('movie_names.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
