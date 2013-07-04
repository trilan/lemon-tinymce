from setuptools import setup, find_packages


setup(
    name = 'lemon-tinymce',
    version = '2.1.1',
    url = 'https://github.com/trilan/lemon-tinymce',
    author = 'Trilan Team',
    author_email = 'dev@lemon.io',
    description = 'A Django application that contains a widget to render a ' \
                  'form field as a TinyMCE editor.',
    packages = find_packages(exclude=['demoproject', 'demoproject.*']),
    include_package_data = True,
    zip_safe = False,
)
