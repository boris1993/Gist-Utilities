#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for getting GitHub Gist from local files
"""
import sys

__author__ = "Boris Zhao"

import json
import requests
import argparse
import readline

import global_config

__arg_parser = argparse.ArgumentParser()


def get_gist(gist_id):
    """
    Get the specified Gist
    :param gist_id:
    :return:
    """

    print("[INFO] Fetching Gist...")
    try:
        resp = requests.get(global_config.API_URL + "/gists/" + gist_id, timeout=5)
    except requests.exceptions.Timeout:
        print("[ERROR] Request timeout. Please try again later. ")
        sys.exit(-1)

    # 200 OK
    if resp.status_code == 200:
        return json.loads(resp.content)
    else:
        print("[ERROR] Failed to fetch the Gist. Details: ")
        print(json.loads(resp.content)["message"])
        return None


def __print_gist(gist, json_format):
    if gist:
        if json_format:
            print(json.dumps(gist, indent=4))
        else:
            print("\n")
            print("Gist Information")
            print("----------------")
            print("ID: " + gist["id"])
            print("Description: " + gist["description"])
            print("Files: ")

            for filename in gist["files"]:
                print("\t" + filename)

            print("----------------")


def __main():
    __init_arg_parser()

    if len(sys.argv) == 1:
        gist_id = input("Gist ID: ")

        if gist_id:
            gist = get_gist(gist_id)

            __print_gist(gist, json_format=False)
        else:
            print("[ERROR] No Gist ID given. Will now exit. ")
            sys.exit(0)
    else:
        args = __arg_parser.parse_args()
        gist = get_gist(args.gist_id)

        __print_gist(gist, args.json)


def __init_arg_parser():
    """
    Initialize arguments
    """

    __arg_parser.add_argument("-g", "--gist-id",
                              help="The Gist ID",
                              action="store",
                              required=True)

    __arg_parser.add_argument("-j", "--json",
                              help="Print the output in JSON format if the Gist exists",
                              action="store_true",
                              required=False)

    __arg_parser.add_argument("-o", "--output",
                              help="Save the output to a file",
                              action="store",
                              required=False)


if __name__ == '__main__':
    try:
        __main()
    except KeyboardInterrupt:
        print("\n[INFO] User cancelled. ")
