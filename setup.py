import os
import sys
import codecs
from setuptools import setup, find_packages


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, str(rel_path)), 'r',encoding="utf-8") as fp:
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
    linter = (line.strip() for line in open(filename,encoding='utf-16'))
    reqs = [line for line in linter if line and not line.startswith("#")]
    if sys.platform == "win32":
        reqs.append('pywin32')
    # if py<=3.6 add dataclasses
    if sys.version_info.major == 3 and sys.version_info.minor <= 6:
        reqs.append("dataclasses")
    if sys.version_info.major == 3 and sys.version_info.minor <= 7:
        reqs.remove("facebook-wda>=1.3.3")
        reqs.append("facebook-wda<1.4.8")
    if is_docker():
        reqs.remove("opencv-contrib-python>=4.4.0.46, <=4.6.0.66")
        reqs.append("opencv-contrib-python-headless==4.5.5.64")
    return reqs


setup(
    name='autopc',
    version=get_version("autopc/utils/utils_version.py"),
    author='orcakill',
    author_email='orcakill@dingtalk.com',
    description='An image recognition framework running on a computer',
    long_description='UI Test Automation Framework for Games and Apps on Android/iOS/Windows, present by NetEase Games',
    url='https://github.com/orcakill/autopc',
    license='Apache License 2.0',
    keywords=['automation', 'opencv-python', 'ocr'],
    packages=find_packages(exclude=['test', 'dist']),
    include_package_data=True,
    install_requires=parse_requirements('requirements.txt'),
    classifiers=[
        'Programming Language :: Python :: 3.9',
    ],
)