from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'hotels.views.home', name='home'),
    url(r'^review/(?P<id>\w{0,256})/$', 'hotels.views.get_review', name='review'),
    url(r'^reviews/add', 'hotels.views.add_review', name='add_review'),
    url(r'^reviews/', 'hotels.views.reviews', name='reviews'),

)