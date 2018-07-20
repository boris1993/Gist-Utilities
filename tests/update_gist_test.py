#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import update_gist
import unittest


class UpdateGistTest(unittest.TestCase):

    def test_update_gist(self):
        print("")
        update_gist.update_gist("2092be9a799f624e3ea3ba8dee031df06e3e38a9",
                                "30022fafc7d718fc18a680d92241ab55",
                                "~/.gitignore_global")


    def test_update_non_existent_gist(self):
        update_gist.update_gist("2092be9a799f624e3ea3ba8dee031df06e3e38a9",
                                "30022fafc7d718fc18a680d92241ab550",
                                "~/.gitignore_global")


    def test_update_non_existent_file(self):
        update_gist.update_gist("2092be9a799f624e3ea3ba8dee031df06e3e38a9",
                                "30022fafc7d718fc18a680d92241ab55",
                                "~/.gitignore_global_non_existent")


if __name__ == '__main__':
    unittest.main()
