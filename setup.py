from distutils.core import setup

setup(
    name='djangoUsps',
    version='0.1.0',
    author='Jesse Gomez',
    author_email='jesse@luxnovalabs.com',
    packages=['djangoUsps'],
    url='http://pypi.python.org/pypi/pyUspsLib/',
    license='LICENSE',
    description='Django wrapper around pyUspsLib. Provides ajax interface and simple object to connect ot USPS.',
    long_description=open('README.md').read(),
    install_requires=[
    ],
)