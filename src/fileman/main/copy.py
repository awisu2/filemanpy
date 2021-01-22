from argparse import ArgumentParser

from fileman.main.share import create_base_argperser
from fileman.copy import copy as _copy


def create_argperser() -> ArgumentParser:
    argperser = create_base_argperser()
    argperser.add_argument(
        "-i",
        "--input",
        type=str,
        required=True,
        help="画像の幅",
    )
    argperser.add_argument(
        "-o",
        "--out",
        type=str,
        required=True,
        help="画像の高さ",
    )
    return argperser


def copy():
    """ファイルのコピー"""

    # パラメータチェック
    args = create_argperser().parse_args()
    input = args.input
    out = args.out
    print(input, out)
    # _copy(args["in"], args.out)
