import shutil
import unittest
from unittest.mock import patch
import sys
from pathlib import Path

from fileman.main import move


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

    def test_copy(self):
        """copy"""
        # ファイルコピー
        argv = self.argv1 + ["-o", str(self.out.resolve())]
        with patch.object(sys, "argv", argv):
            move.copy()
            self.assertTrue(self.out.is_file())

        # コピー先がディレクトリ
        argv = self.argv1 + ["-o", str(self.out_dir.resolve())]
        with patch.object(sys, "argv", argv):
            move.copy()
            self.assertTrue((self.out_dir / self.input.name).is_file())

    def test_copy_multi(self):
        """copy multi input"""
        # ファイルコピー
        argv = self.argv2 + ["-o", str(self.out.resolve())]
        with patch.object(sys, "argv", argv):
            move.copy()
            # 同じファイル名でコピーされるので１ファイルだけ
            self.assertTrue(self.out.is_file())

        # コピー先がディレクトリ
        argv = self.argv2 + ["-o", str(self.out_dir.resolve())]
        with patch.object(sys, "argv", argv):
            move.copy()
            self.assertTrue((self.out_dir / self.inputs[0].name).is_file())
            self.assertTrue((self.out_dir / self.inputs[1].name).is_file())

    def test_copy_adddirname(self):
        """addDirName"""
        # コピー先がディレクトリ
        argv = self.argv1 + ["-o", str(self.out.resolve()), "--addDirName"]
        with patch.object(sys, "argv", argv):
            move.copy()
            _out = self.out_dir / (self.input.parent.name + "_" + self.out.name)
            self.assertTrue(_out.is_file())

        # コピー先がディレクトリ
        argv = self.argv1 + ["-o", str(self.out_dir.resolve()), "--addDirName"]
        with patch.object(sys, "argv", argv):
            move.copy()
            _out = self.out_dir / (self.input.parent.name + "_" + self.input.name)
            self.assertTrue(_out.is_file())

    def test_copy_withdir(self):
        """addDirName"""
        # コピー先がディレクトリ
        argv = self.argv1 + ["-o", str(self.out_dir.resolve()), "--withDir"]
        with patch.object(sys, "argv", argv):
            move.copy()
            _out = self.out_dir / self.input.parent.name / self.input.name
            self.assertTrue(_out.is_file())

        # addDirNameも一緒
        argv = self.argv1 + [
            "-o",
            str(self.out_dir.resolve()),
            "--withDir",
            "--addDirName",
        ]
        with patch.object(sys, "argv", argv):
            move.copy()
            _out = (
                self.out_dir
                / self.input.parent.name
                / (self.input.parent.name + "_" + self.input.name)
            )
            self.assertTrue(_out.is_file())

    def test_copy_outisdir(self):
        """outIsDir"""

        # 出力先を強制ディレクトリ扱い
        argv = self.argv1 + ["-o", str(self.out2.resolve()), "--outIsDir"]
        with patch.object(sys, "argv", argv):
            move.copy()
            _out = self.out2 / self.input.name
            self.assertTrue(_out.is_file())
