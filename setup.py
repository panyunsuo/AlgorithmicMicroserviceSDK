"""
@File    :   setup.py.py
@Contact :   panrs@venpoo.com

@Modify Time
------------
2020/7/14 16:24
------------
@Model Name:   安装命令:python setup.py install
"""
from setuptools import find_packages, setup

PACKAGE = 'algorithm_mic_sdk'

with open("README.rst", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

VERSION = __import__(PACKAGE).__version__
setup(
    name="leqi-algorithm-mic-sdk",
    version=VERSION,
    description="LeQi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="panso",
    author_email="panrs@venpoo.com",
    packages=find_packages(where='.', exclude=(), include=('*',)),
    include_package_data=True,
    platforms="any",
    install_requires=['requests', 'websocket-client'],
    url='https://www.yuque.com/fenfendeyouzhiqingnian/algorithm'
)
