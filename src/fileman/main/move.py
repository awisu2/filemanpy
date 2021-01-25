from typing import List
from argparse import ArgumentParser
from pathlib import Path

from fileman.main.share import create_base_argperser, create_check_help_argperser
from fileman.move import copy as _copy, move as _move


def create_argperser() -> ArgumentParser:
    argperser = create_base_argperser()
    argperser.add_argument(
        "-i", "--input", type=str, required=True, help="画像の幅", nargs="+"
    )
    argperser.add_argument("-o", "--out", type=str, required=True, help="画像の高さ")
    argperser.add_argument(
        "--addDirName", action="store_true", help="コピー時のファイル名に、ディレクトリ名を追加"
    )
    argperser.add_argument("--withDir", action="store_true", help="コピー元のディレクトリも同時に移動")
    argperser.add_argument("--outIsDir", action="store_true", help="outをディレクトリとする")
    argperser.add_argument(
        "-r",
        "--recursive",
        type=int,
        default=1,
        help="inputにディレクトリが割り当てられたときに、サブディレクトリも対象とする。0で全サブディレクトリ",
    )

    return argperser


def _get_children(path: Path, *, recursive=1, recursive_count=1) -> List[Path]:
    if path.is_file():
        return [path]

    pathes = []
    if path.is_dir():
        for _path in path.glob("*"):
            if _path.is_file():
                pathes.append(_path)
            elif _path.is_dir():
                if recursive == 0 or recursive > recursive_count:
                    pathes += _get_children(_path, recursive_count=recursive_count + 1)

    return pathes


def _run(func):
    # helpのチェック(requiredが引っかかるので、最小のperserでチェック)
    args = create_check_help_argperser().parse_args()
    if args.help:
        create_argperser().print_help()
        return

    # 処理
    args = create_argperser().parse_args()
    for input in args.input:
        # ディレクトリであれば基準パスを取得
        pathes = [input]
        base_path = None
        input = Path(input)
        if input.is_dir():
            base_path = input.parent
            pathes = _get_children(Path(input), recursive=args.recursive)

        for path in pathes:
            func(
                path,
                args.out,
                addDirName=args.addDirName,
                withDir=args.withDir,
                outIsDir=args.outIsDir,
                base_path=base_path,
            )


def move():
    """ファイルの移動
    moveとcopyは基本的に同じ引数で動作するため、最後のメソッド呼び出しだけ違う
    """
    _run(_move)


def copy():
    """ファイルのコピー
    moveとcopyは基本的に同じ引数で動作するため、最後のメソッド呼び出しだけ違う
    """
    _run(_copy)
