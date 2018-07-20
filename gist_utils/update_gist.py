#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for updating GitHub Gist from local files
"""
__author__ = "Boris Zhao"

import os
import sys
import json
import argparse
import readline
import requests

import global_config
import get_gist

from utils import common_utils

__arg_parser = argparse.ArgumentParser()

CONFIG = common_utils.read_config()
API_URL = CONFIG["GitHub"]["API_URL"]


def update_gist(token, gist_id, files):
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
        sys.exit(-1)

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

            # Pick out the filename from the last part of the path to the file
            filename = file.split(os.sep)[-1]
            data["files"][filename] = file_info
        except IOError:
            print("[ERROR] " + file + " not found. Skipping to next one. ")

    # If the "files" section is empty
    if not data['files']:
        print("[ERROR] No file added. Process stopped. ")
        sys.exit(-1)

    description = input("Description (Leave this blank to remain untouched): ")

    headers = {"Authorization": "token " + token}

    if description:
        data["description"] = description

    print("[INFO] Updating Gist...")
    try:
        resp = requests.patch(global_config.API_URL + "/gists/" + gist_id,
                              headers=headers,
                              data=json.dumps(data),
                              timeout=5)
    except requests.exceptions.Timeout:
        print("[ERROR] Request timeout. Please try again later. ")
        sys.exit(-1)

    # 200 OK
    if resp.status_code == 200:
        print("[INFO] Gist updated")
    else:
        print("[ERROR] Failed to update the Gist. Details: ")
        print(json.loads(resp.content)["message"])


def __main():
    __init_arg_parser()

    if len(sys.argv) == 1:
        __arg_parser.print_help()
        sys.exit(0)

    args = __arg_parser.parse_args()

    update_gist(args.token, args.gist_id, args.file)


def __init_arg_parser():
    """
    Initialize arguments
    """
    __arg_parser.add_argument("-t", "--token",
                              help="The access token for logging in",
                              action="store",
                              required=True)

    __arg_parser.add_argument("-g", "--gist-id",
                              help="The Gist ID",
                              action="store",
                              required=True)

    __arg_parser.add_argument("-f", "--file",
                              help="A list of file going to be uploaded to your Gist. "
                                   "Either absolute path or relative path are accepted. ",
                              nargs="+",
                              required=True)


if __name__ == '__main__':
    try:
        __main()
    except KeyboardInterrupt:
        print("\n[INFO] User cancelled. ")
