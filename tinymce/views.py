# Copyright (c) 2008 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)

from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.shortcuts import render
from django.utils import simplejson
from django.utils.translation import ugettext as _

from tinymce.widgets import get_language_config


def textareas_js(request, name, lang=None):
    """
    Returns a HttpResponse whose content is a JavaScript file. The template
    is loaded from 'tinymce/<name>_textareas.js' or
    '<name>/tinymce_textareas.js'. Optionally, the lang argument sets the
    content language.
    """
    template_files = (
        'tinymce/%s_textareas.js' % name,
        '%s/tinymce_textareas.js' % name,
    )
    template = loader.select_template(template_files)

    vars = get_language_config(lang)
    vars['content_language'] = lang
    context = RequestContext(request, vars)

    return HttpResponse(template.render(context),
            content_type="application/x-javascript")


def preview(request, name):
    """
    Returns a HttpResponse whose content is an HTML file that is used
    by the TinyMCE preview plugin. The template is loaded from
    'tinymce/<name>_preview.html' or '<name>/tinymce_preview.html'.
    """
    template_files = (
        'tinymce/%s_preview.html' % name,
        '%s/tinymce_preview.html' % name,
    )
    template = loader.select_template(template_files)
    return HttpResponse(template.render(RequestContext(request)),
            content_type="text/html")


def filebrowser_js(request):
    url = request.GET.get('url')
    if not url:
        raise Http404
    return render(request, 'tinymce/filebrowser.js', {'url': url},
                  content_type='application/x-javascript')
