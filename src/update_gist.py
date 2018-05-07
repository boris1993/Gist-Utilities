#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for updating GitHub Gist from local files
"""

__author__ = "Boris Zhao"

import json
import os
import requests

import common_utils
import global_config
import get_gist


def update_gist(token, gist_id, *files):
    """
    Update files in this Gist
    :param token: Your GitHub access token
    :param gist_id: The Gist you want to update
    :param files: Path to files you want to update
    :return:
    """

    gist_info = get_gist.get_gist(gist_id)

    if gist_info is None:
        print("[ERROR] The specified Gist does not exist")
        return

    data = {
        "files": {}
    }

    for file in files:
        if file[0] == "~":
            path = os.path.expanduser(file)
        else:
            path = os.path.abspath(file)

        try:
            file_info = {
                "content": common_utils.read_content(path)
            }
            data["files"][file.split("/")[-1]] = file_info
        except IOError:
            print("[ERROR] " + file + " not found. Skipping to next one. ")

    # If the "files" section is empty
    if not data['files']:
        print("[ERROR] No file added. Process stopped. ")
        return

    description = input("Description (Leave this blank to remain untouched): ")

    headers = {"Authorization": "token " + token}

    if description:
        data["description"] = description

    print("[INFO] Updating Gist...")
    resp = requests.post(global_config.API_URL + "/gists/" + gist_id, headers=headers, data=json.dumps(data), timeout=5)

    # 200 OK
    if resp.status_code == 200:
        print("[INFO] Gist updated")
    else:
        print("[ERROR] Failed to update the Gist. Details: ")
        print(json.loads(resp.content)["message"])


def __main():
    return


if __name__ == '__main__':
    __main()
