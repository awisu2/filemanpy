import unittest


class TestSample(unittest.TestCase):
    def setUp(self):
        self.value = range(3)

    def tearDown(self):
        self.value = None

    def test_hello(self):
        self.assertEqual("hello", "hello")
