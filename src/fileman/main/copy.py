from argparse import ArgumentParser

from fileman.main.share import create_base_argperser
from fileman.copy import copy as _copy


def _get_argperser() -> ArgumentParser:
    argperser = create_base_argperser()
    return argperser


def copy():
    """結合処理"""

    # パラメータチェック
    args = _get_argperser().parse_args()
    _copy(args)
