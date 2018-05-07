#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for getting GitHub Gist from local files
"""

__author__ = "Boris Zhao"

import json
import requests

import global_config


def get_gist(gist_id):
    """
    Get the specified Gist
    :param gist_id:
    :return:
    """

    print("[INFO] Fetching Gist...")
    resp = requests.get(global_config.API_URL + "/gists/" + gist_id, timeout=5)

    # 200 OK
    if resp.status_code == 200:
        return json.loads(resp.content)
    else:
        print("[ERROR] Failed to fetch the Gist. Details: ")
        print(json.loads(resp.content)["message"])
        return None


def __main():
    return


if __name__ == '__main__':
    __main()
