from argparse import ArgumentParser

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

    return argperser


def move():
    """ファイルのコピー
    moveとcopyは基本的に同じ引数で動作するため、最後のメソッド呼び出しだけ違う
    """
    # helpのチェック(requiredが引っかかるので、最小のperserでチェック)
    args = create_check_help_argperser().parse_args()
    if args.help:
        create_argperser().print_help()
        return

    # 処理
    args = create_argperser().parse_args()
    for input in args.input:
        _move(
            input,
            args.out,
            addDirName=args.addDirName,
            withDir=args.withDir,
            outIsDir=args.outIsDir,
        )


def copy():
    """ファイルのコピー
    moveとcopyは基本的に同じ引数で動作するため、最後のメソッド呼び出しだけ違う
    """
    # helpのチェック(requiredが引っかかるので、最小のperserでチェック)
    args = create_check_help_argperser().parse_args()
    if args.help:
        create_argperser().print_help()
        return

    # 処理
    args = create_argperser().parse_args()
    for input in args.input:
        _copy(
            input,
            args.out,
            addDirName=args.addDirName,
            withDir=args.withDir,
            outIsDir=args.outIsDir,
        )