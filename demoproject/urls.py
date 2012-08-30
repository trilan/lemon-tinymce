import lemon

from django.conf import settings
from django.conf.urls.defaults import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin


admin.autodiscover()
urlpatterns = patterns('',
    url(r'^admin/', include(lemon.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
