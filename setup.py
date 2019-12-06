#!/usr/bin/env python

from setuptools import setup, find_packages
from codecs import open
import os


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


install_requires = read("requirements.txt")

setup(
    name="account-links-generator",
    author="HMRC Platform Security",
    version=read(".version"),
    description="Generate accountlinks.md from aws-users' config.yaml",
    url="https://github.com/hmrc/account-links-generator",
    long_description=read("README.md"),
    platforms=["Linux"],
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "account-links-generator = accountlinks_generator.accountlinks_generator:main"
        ]
    },
)
