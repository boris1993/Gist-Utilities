#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import common_utils
import unittest


class ReadConfigTest(unittest.TestCase):

    def test_read_config(self):
        config = common_utils.read_config()
        items = config.sections()
        print(items)


if __name__ == '__main__':
    unittest.main()
