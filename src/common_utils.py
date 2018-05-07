#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Common utilities
"""

__author__ = "Boris Zhao"


def read_content(path):
    """
    Read the content of the file

    :param path: Path to the file
    :return: Content of the file
    :rtype: str
    """
    with open(path, "r") as f:
        return f.read()
