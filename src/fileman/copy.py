from typing import Union

from pathlib import Path
import shutil

strPath = Union[str, Path]


def copy(src: strPath, dist: strPath, *, addDirName=False):
    """ファイルをコピー

    保存先のディレクトリがない場合は作成
    保存先がディレクトリの場合は、その配下にコピー

    Args:
        src (strPath): [description]
        dist (strPath): [description]
        addDirName (bool, optional): [description]. Defaults to False.
    """
    _src = Path(src)
    _dist = Path(dist)

    if not _src.is_file():
        return False

    if _dist.is_dir():
        _dist = _dist / _src.name

    if addDirName:
        _dist = _dist.parent / (_src.parent.name + "_" + _dist.name)

    # コピー先のディレクトリを作成
    if not _dist.parent.is_dir():
        _dist.parent.mkdir(parents=True, exist_ok=True)

    shutil.copy(_src, _dist)
