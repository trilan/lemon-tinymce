from django.db import models
from django.contrib import admin

from pages.models import Page
from tinymce.widgets import TinyMCE


class TinyMCEPageAdmin(admin.ModelAdmin):
    
    formfield_overrides = {models.TextField: {'widget': TinyMCE}}


admin.site.register(Page, TinyMCEPageAdmin)
