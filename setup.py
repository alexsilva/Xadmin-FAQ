from distutils.core import setup
import os

basedir = os.path.dirname(os.path.basename(__file__))

try:
    from pip.req import parse_requirements
    from pip.download import PipSession

    install_reqs = parse_requirements(os.path.join(basedir, 'requirements.txt'),
                                      session=PipSession())

    install_reqs = [str(ir.req) for ir in install_reqs]

except ImportError:
    install_reqs = []

setup(
    name='xadmin-mptt-plugin',
    version='1.0',
    packages=['xplugin'],
    url='https://github.com/alexsilva/Xadmin-FAQ',
    license='MIT',
    author='alex',
    author_email='',
    description='Xadmin plugin editing templates on the tree',
    install_reqs=install_reqs
)
