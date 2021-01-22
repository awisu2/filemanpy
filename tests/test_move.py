import shutil
import unittest
from unittest.mock import patch
import sys
from pathlib import Path

from src.fileman.main import move


class TestCopy(unittest.TestCase):
    assets_dir: Path

    def setUp(self):
        self.assets_dir = Path("tests/.assets")
        self.assets_dir.mkdir(parents=True, exist_ok=True)

        self.inputs = [
            self.assets_dir / "input.txt",
            self.assets_dir / "input2.txt",
        ]
        self.out_dir = self.assets_dir / "out"
        self.out = self.out_dir / "out.txt"
        self.out2 = self.out_dir / "out2.txt"

        self.input = self.inputs[0]
        for input in self.inputs:
            input.touch(exist_ok=True)
        self.argv1 = ["_", "copy", "-i", str(self.input.resolve())]
        self.argv2 = [
            "_",
            "copy",
            "-i",
        ]
        for input in self.inputs:
            self.argv2 += [str(input.resolve())]

    def tearDown(self):
        shutil.rmtree(self.assets_dir)

    def test_move(self):
        """copy"""
        # ファイルコピー
        argv = self.argv1 + ["-o", str(self.out.resolve())]
        with patch.object(sys, "argv", argv):
            move.move()
            self.assertTrue(self.out.is_file())
            self.assertFalse(self.input.exists())
