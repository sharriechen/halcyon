from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'halcyon.views.home', name='home'),
    # url(r'^halcyon/', include('halcyon.foo.urls')),

    url(r'^login/$', 'django.contrib.auth.views.login'),

    url(r'^todo/todo/', 'todo.views.todo'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^todo/', include('todo.urls'))
)
