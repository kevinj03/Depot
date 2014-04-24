from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from depotapp.views import login_view,logout_view


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'depot.views.home', name='home'),
    # url(r'^depot/', include('depot.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^depotapp/', include('depotapp.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', login_view),
    (r'accounts/logout/$', logout_view),
)
urlpatterns += staticfiles_urlpatterns()
