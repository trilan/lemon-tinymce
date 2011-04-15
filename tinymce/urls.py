from django.conf.urls.defaults import patterns, url
from tinymce.views import filebrowser_js


urlpatterns = patterns('',
    url(r'^filebrowser.js', filebrowser_js, name='tinymce_filebrowser_js'),
)
