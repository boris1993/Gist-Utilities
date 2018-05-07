#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for creating GitHub Gist from local files
"""

__author__ = "Boris Zhao"

import os
import sys
import argparse
import requests
import json

import global_config
import common_utils

__arg_parser = argparse.ArgumentParser()


def create_gist(files, is_private, token):
    """
    Create the Gist

    :param files: A list of files to be added to the Gist
    :param is_private: Is this a private Gist?
    :param token: Your GitHub access token
    :return:
    """
    description = input("(Optional) Description: ")

    headers = {"Authorization": "token " + token}

    data = {
        "description": description,
        "public": not is_private,
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

    print("[INFO] Creating Gist...")
    resp = requests.post(global_config.API_URL + "/gists", headers=headers, data=json.dumps(data), timeout=5)

    # 201 Created
    if resp.status_code == 201:
        print("[INFO] Gist created")
        json_resp = json.loads(resp.content)
        print("[INFO] Gist URL: " + json_resp["html_url"])
        print("[INFO] Raw file URL: " + json_resp["url"])
    else:
        print("[ERROR] Failed to create the Gist. Details: ")
        print(json.loads(resp.content)["message"])


def __main():
    __init_arg_parser()

    if len(sys.argv) == 1:
        __arg_parser.print_help()
        sys.exit(0)

    args = __arg_parser.parse_args()

    create_gist(args.file, args.private, args.token)


def __init_arg_parser():
    """
    Initialize arguments
    """
    __arg_parser.add_argument("-t", "--token",
                              help="The access token for logging in",
                              action="store",
                              required=True)

    __arg_parser.add_argument("-f", "--file",
                              help="A list of file going to be uploaded to your Gist. "
                              "Either absolute path or relative path are accepted. ",
                              nargs="+",
                              required=True)

    __arg_parser.add_argument("--private",
                              help="Create a private Gist instead of a public Gist",
                              action="store_true")

    __arg_parser.set_defaults(private=False)


if __name__ == '__main__':
    __main()
