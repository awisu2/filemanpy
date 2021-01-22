import unittest
from unittest.mock import patch
from src.fileman.main import copy
import sys


class TestCopy(unittest.TestCase):
    def setUp(self):
        # self.value = range(3)
        pass

    def tearDown(self):
        # self.value = None
        pass

    def test_hello(self):
        try:
            argvs = (
                # ["copy", "copy"],
                # ["copy", "-i", "foo", "-o", "bar", "copy"],
                ["_module", "copy", "-i", "foo", "-o", "bar"],
            )
            for argv in argvs:
                with patch.object(sys, "argv", argv):
                    copy.copy()
        except Exception as e:
            print(e)

        # self.assertEqual("hello", "hello")
