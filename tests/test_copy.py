import shutil
import unittest
from unittest.mock import patch
import sys
from pathlib import Path

from src.fileman.main import copy


class TestCopy(unittest.TestCase):
    assets_dir: Path

    def setUp(self):
        self.assets_dir = Path("tests/.assets")
        self.assets_dir.mkdir(parents=True, exist_ok=True)

        self.input = self.assets_dir / "input.txt"
        self.out_dir = self.assets_dir / "out"
        self.out = self.out_dir / "out.txt"

        self.input.touch(exist_ok=True)
        self.arr = ["_", "copy", "-i", str(self.input.resolve())]

    def tearDown(self):
        shutil.rmtree(self.assets_dir)

    def test_copy(self):
        """copy"""
        # ファイルコピー
        argv = self.arr + ["-o", str(self.out.resolve())]
        with patch.object(sys, "argv", argv):
            copy.copy()
            self.assertTrue(self.out.is_file())

        # コピー先がディレクトリ
        argv = self.arr + ["-o", str(self.out_dir.resolve())]
        with patch.object(sys, "argv", argv):
            copy.copy()
            self.assertTrue((self.out_dir / self.input.name).is_file())

    def test_copy_adddirname(self):
        """addDirName"""
        # コピー先がディレクトリ
        argv = self.arr + ["-o", str(self.out.resolve()), "--addDirName"]
        with patch.object(sys, "argv", argv):
            copy.copy()
            _out = self.out_dir / (self.input.parent.name + "_" + self.out.name)
            self.assertTrue(_out.is_file())

        # コピー先がディレクトリ
        argv = self.arr + ["-o", str(self.out_dir.resolve()), "--addDirName"]
        with patch.object(sys, "argv", argv):
            copy.copy()
            _out = self.out_dir / (self.input.parent.name + "_" + self.input.name)
            self.assertTrue(_out.is_file())

    def test_copy_withdir(self):
        """addDirName"""
        # コピー先がディレクトリ
        argv = self.arr + ["-o", str(self.out_dir.resolve()), "--withDir"]
        with patch.object(sys, "argv", argv):
            copy.copy()
            _out = self.out_dir / self.input.parent.name / self.input.name
            self.assertTrue(_out.is_file())

        # addDirNameも一緒
        argv = self.arr + [
            "-o",
            str(self.out_dir.resolve()),
            "--withDir",
            "--addDirName",
        ]
        with patch.object(sys, "argv", argv):
            copy.copy()
            _out = (
                self.out_dir
                / self.input.parent.name
                / (self.input.parent.name + "_" + self.input.name)
            )
            self.assertTrue(_out.is_file())
