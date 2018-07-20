#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Global configurations
"""

from utils import common_utils

# GitHub API address
# API_URL = "https://api.github.com"
API_URL = common_utils.read_config().get("GitHub", "API_URL")

TOKEN = common_utils.read_config().get("User", "TOKEN")
