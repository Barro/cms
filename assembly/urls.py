from django.conf.urls import url, include, patterns
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings

from filebrowser.sites import site

admin.autodiscover()

urlpatterns = i18n_patterns('',
                            url(r'^ckeditor/', include('ckeditor.urls')),
                            url(r'^admin/filebrowser/', include(site.urls)),
                            url(r'^admin/', include(admin.site.urls)),
                            url(r'^blog/', include('blog.urls')),
                            url(r'^', include('cms.urls')),)

if settings.DEBUG:
    urlpatterns = patterns('',
                           url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                               {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                           url(r'', include('django.contrib.staticfiles.urls')),) + urlpatterns