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

with open("README.MD", "r") as fh:
    long_description = fh.read()

setup(
    name="algorithm-mic-sdk",
    version="0.0.3",
    description="LeQi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT Licence",
    author="panso",
    author_email="panrs@venpoo.com",
    packages=find_packages(where='.', exclude=(), include=('*',)),
    include_package_data=True,
    platforms="any",
    install_requires=['requests']
)
