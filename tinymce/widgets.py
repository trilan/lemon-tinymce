# Copyright (c) 2008 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)

"""
This TinyMCE widget was copied and extended from this code by John D'Agostino:
http://code.djangoproject.com/wiki/CustomWidgetsTinyMCE
"""

from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse
from django.forms.widgets import flatatt
from django.utils.encoding import smart_unicode
from django.utils.html import escape
from django.utils import simplejson
from django.utils.datastructures import SortedDict
from django.utils.safestring import mark_safe
from django.utils.translation import get_language, ugettext as _

import tinymce.settings


class TinyMCE(forms.Textarea):
    """
    TinyMCE widget. Set settings.TINYMCE_JS_URL to set the location of the
    javascript file. Default is "STATIC_URL + 'js/tiny_mce/tiny_mce.js'".
    You can customize the configuration with the mce_attrs argument to the
    constructor.

    In addition to the standard configuration you can set the
    'content_language' parameter. It takes the value of the 'language'
    parameter by default.
    """

    def __init__(self, content_language=None, attrs=None, mce_attrs=None):
        super(TinyMCE, self).__init__(attrs)
        if mce_attrs is None:
            mce_attrs = {}
        self.mce_attrs = mce_attrs
        if content_language is None:
            content_language = mce_attrs.get('language', None)
        self.content_language = content_language

    def render(self, name, value, attrs=None):
        if value is None: value = ''
        value = smart_unicode(value)
        final_attrs = self.build_attrs(attrs)
        final_attrs['name'] = name
        assert 'id' in final_attrs, "TinyMCE widget attributes must contain 'id'"

        mce_config = self.default_config
        mce_config.update(get_language_config(self.content_language))
        mce_config.update(self.mce_attrs)
        mce_config['mode'] = 'exact'
        mce_config['elements'] = final_attrs['id']
        mce_config['strict_loading_mode'] = 1
        mce_json = simplejson.dumps(mce_config)

        html = [u'<textarea%s>%s</textarea>' % \
            (flatatt(final_attrs), escape(value))]
        html.append(u'<script type="text/javascript">tinyMCE.init(%s)</script>' % mce_json)

        return mark_safe(u'\n'.join(html))
    
    def _default_config(self):
        return tinymce.settings.DEFAULT_CONFIG.copy()
    default_config = property(_default_config)

    def _media(self):
        js = [tinymce.settings.JS_URL]
        return forms.Media(js=js)
    media = property(_media)


class AdminTinyMCE(TinyMCE):

    def __init__(self, content_language=None, attrs=None, mce_attrs=None):
        super(AdminTinyMCE, self).__init__(content_language, attrs, mce_attrs)
        if 'filebrowser' in settings.INSTALLED_APPS:
            self.mce_attrs['file_browser_callback'] = 'lemonFileBrowser'

    @property
    def filebrowser_url(self):
        return reverse('admin:filebrowser:browse')

    def _media(self):
        media = super(AdminTinyMCE, self)._media()
        media.add_js(['%s?url=%s' % (
            reverse('tinymce_filebrowser_js'),
            self.filebrowser_url,
        )])
        return media
    media = property(_media)


def get_language_config(content_language=None):
    language = get_language()[:2]
    if content_language:
        content_language = content_language[:2]
    else:
        content_language = language

    config = {}
    config['language'] = language

    lang_names = SortedDict()
    for lang, name in settings.LANGUAGES:
        if lang[:2] not in lang_names: lang_names[lang[:2]] = []
        lang_names[lang[:2]].append(_(name))
    sp_langs = []
    for lang, names in lang_names.items():
        if lang == content_language:
            default = '+'
        else:
            default = ''
        sp_langs.append(u'%s%s=%s' % (default, ' / '.join(names), lang))

    config['spellchecker_languages'] = ','.join(sp_langs)

    if content_language in settings.LANGUAGES_BIDI:
        config['directionality'] = 'rtl'
    else:
        config['directionality'] = 'ltr'

    return config
