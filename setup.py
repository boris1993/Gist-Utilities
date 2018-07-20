#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from setuptools import setup, find_packages

REQUIRED_PACKAGES = [
    "requests"
]

setup(
    name="gist-utils",
    version="0.0.1",
    description="A set of utilities for manipulating your GitHub Gists",
    long_description=open("README.md").read(),
    author="Boris Zhao",
    author_email="boris1993@126.com",
    url="",
    license="MIT",
    packages=find_packages(exclude=("tests", "docs", "etc")),
    test_suite="tests",
    install_requires=REQUIRED_PACKAGES
)
