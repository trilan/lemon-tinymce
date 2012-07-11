from django.conf import settings


DEFAULT_CONFIG = getattr(settings, 'TINYMCE_DEFAULT_CONFIG', {
    'convert_urls': False,
    'height': '350',
    'theme': 'advanced',
    'plugins': 'advimage,advlink,fullscreen,media,safari,table,paste',
    'theme_advanced_toolbar_location': 'top',
    'theme_advanced_buttons1': 'fullscreen,|,bold,italic,underline,'
                               'strikethrough,|,justifyleft,justifycenter,'
                               'justifyright,justifyfull,|,'
                               'forecolor,backcolor,|,'
                               'formatselect,fontselect,fontsizeselect',
    'theme_advanced_buttons2': 'cut,copy,paste,pastetext,pasteword,|,'
                               'bullist,numlist,|,outdent,indent,'
                               'blockquote,|,sub,sup,|,undo,redo,|,'
                               'link,unlink,anchor,image,cleanup,help,code',
    'theme_advanced_buttons3': 'tablecontrols,|,hr,removeformat,visualaid,'
                               '|,charmap,media',
    'theme_advanced_toolbar_align': 'center',
    'theme_advanced_statusbar_location': 'bottom',
    'theme_advanced_resizing': 'true',
})

DEFAULT_CONFIG.update(getattr(settings, 'TINYMCE_CONFIG', {}))

JS_URL = getattr(settings, 'TINYMCE_JS_URL',
                 '%stinymce/js/tiny_mce.js' % settings.STATIC_URL)
