from setuptools import setup, find_packages


setup(
    name = 'trilan-tinymce',
    version = '2.0',
    url = 'https://github.com/trilan/trilan-tinymce',
    author = 'Mike Yumatov',
    author_email = 'lemon@trilandev.com',
    description = 'A Django application that contains a widget to render a ' \
                  'form field as a TinyMCE editor.',
    packages = find_packages(exclude=['demoproject', 'demoproject.*']),
    include_package_data = True,
    zip_safe = False,
)
