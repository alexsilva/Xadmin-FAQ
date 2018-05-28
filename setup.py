import os

from setuptools import setup

basedir = os.path.dirname(os.path.basename(__file__))

setup(
    name='xadmin-mptt-plugin',
    version='1.0',
    packages=['xplugin'],
    url='https://github.com/alexsilva/xadmin-mppt-plugin',
    license='MIT',
    author='alex',
    author_email='',
    description='Xadmin plugin editing templates on the tree',
    install_requires=["django-mptt"]
)
