import unittest
from pathlib import Path


class TestSample(unittest.TestCase):
    def setUp(self):
        self.value = range(3)

    def tearDown(self):
        self.value = None

    def test_hello(self):
        print("----------")
        src = Path("src")
        for path in src.glob("**/*"):
            rel = path.relative_to(src)

            dirs = []
            path = rel
            while True:
                path = path.parent
                if path == Path("."):
                    break
                dirs.append(path.name)
            d = "_".join(dirs)
            print(rel, ":" + d)
