from argparse import ArgumentParser

from fileman.main.share import create_base_argperser
from fileman.copy import copy as _copy


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
    return argperser


def copy():
    """ファイルのコピー"""
    args = create_argperser().parse_args()
    out = args.out

    for input in args.input:
        _copy(input, out, addDirName=args.addDirName, withDir=args.withDir)
