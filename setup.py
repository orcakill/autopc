import os
import sys
import codecs
from setuptools import setup, find_packages


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, str(rel_path)), 'r', encoding="utf-8") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            # __version__ = "1.x.x"
            deli = '"' if '"' in line else "'"
            return line.split(deli)[1]
    else:
        raise RuntimeError("Unable to find version string.")


def is_docker():
    if os.path.exists('/proc/self/cgroup'):
        with open('/proc/self/cgroup', 'rt') as ifh:
            return 'docker' in ifh.read()
    return False


def parse_requirements(filename):
    """ load requirements from a pip requirements file. (replacing from pip.req import parse_requirements)"""
    linter = (line.strip() for line in open(filename))
    reqs = [line for line in linter if line and not line.startswith("#")]
    if sys.platform == "win32":
        reqs.append('pywin32')
    return reqs


setup(
    name='autopc',
    version=get_version("autopc/utils/utils_version.py"),
    author='orcakill',
    author_email='orcakill@dingtalk.com',
    description='An image recognition framework running on a computer',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/orcakill/autopc',
    license='Apache License 2.0',
    keywords=['automation', 'opencv-python', 'ocr'],
    packages=find_packages(exclude=['test', 'test.*', 'dist', 'dist.*']),
    include_package_data=True,
    install_requires=parse_requirements('requirements.txt'),
    extras_require={
        'test': [
            'nose',
        ],
        'docs': [
            'sphinx',
            'recommonmark',
            'sphinx_rtd_theme',
            'mock',
        ]},
    classifiers=[
        'Programming Language :: Python :: 3.9',
    ],
)
