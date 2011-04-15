from lemon import extradmin
from pages.models import Page


extradmin.site.register(Page, markup_fields=['content'])
