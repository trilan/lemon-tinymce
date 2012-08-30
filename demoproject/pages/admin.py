import lemon
from pages.models import Page


lemon.site.register(Page, markup_fields=['content'])
