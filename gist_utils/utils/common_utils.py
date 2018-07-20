#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Common utilities
"""

import configparser
import os

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


def read_config():
    config = configparser.ConfigParser()

    config.read(os.path.join(os.path.abspath(os.path.dirname("../etc/config.ini")), "config.ini"))
    return config
