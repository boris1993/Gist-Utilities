#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import get_gist
import unittest


class GetGistTest(unittest.TestCase):

    def test_get_correct_gist(self):
        get_gist.get_gist("30022fafc7d718fc18a680d92241ab55")


    def test_get_non_exist_gist(self):
        get_gist.get_gist("30022fafc7d718fc18a680d92241ab550")


if __name__ == '__main__':
    unittest.main()
