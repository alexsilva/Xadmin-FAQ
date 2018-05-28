import os

from setuptools import setup

basedir = os.path.dirname(os.path.basename(__file__))

try:
    # noinspection PyUnresolvedReferences
    import requirements_parser

    install_requires = requirements_parser.parse(os.path.join(basedir, 'requirements.txt'))
except ImportError:
    install_requires = []

setup(
    name='xadmin-mptt-plugin',
    version='1.0',
    packages=['xplugin'],
    url='https://github.com/alexsilva/xadmin-mppt-plugin',
    license='MIT',
    author='alex',
    author_email='',
    description='Xadmin plugin editing templates on the tree',
    install_requires=install_requires
)
