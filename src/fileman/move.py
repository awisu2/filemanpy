from typing import Union, Tuple

from pathlib import Path
import shutil

strPath = Union[str, Path]
returnStrPath = Union[str, Path, None]


def __ready_move(
    src: strPath, dist: strPath, *, addDirName=False, withDir=False, outIsDir=False
) -> Tuple[bool, returnStrPath, returnStrPath]:
    """ファイルの移動準備

    保存先のディレクトリがない場合は作成
    保存先がディレクトリの場合は、その配下にコピー

    Args:
        src (strPath): 移動元ファイル
        dist (strPath): 移動先
        addDirName (bool, optional): 移動先のファイルにディレクトリ名を付与. Defaults to False.
        withDir (bool, optional): 元のディレクトリと同じ名前のディレクトリを作成. Defaults to False.
        outDir (bool, optional): 出力先をディレクトリとして扱う. Defaults to False.

    Returns:
        [type]: [description]
    """
    _src = Path(src)
    _dist = Path(dist)

    if not _src.is_file():
        print(f"{_src.resolve()} is not file")
        return False, None, None

    # srcのディレクトリを付与(強制的にdistをディレクトリ扱いにする)
    if withDir:
        _dist = _dist / _src.parent.name / _src.name

    elif outIsDir or _dist.is_dir():
        _dist = _dist / _src.name

    # ファイル名にsrcのディレクトリ名を付与
    if addDirName:
        _dist = _dist.parent / (_src.parent.name + "_" + _dist.name)

    # コピー先のディレクトリを作成
    if not _dist.parent.is_dir():
        if _dist.parent.exists():
            print(f"{_dist.parent.resolve()} is not directory")
            return False, None, None
        _dist.parent.mkdir(parents=True, exist_ok=True)

    return True, _src, _dist


def copy(*args, **kwargs) -> bool:
    ok, src, dist = __ready_move(*args, **kwargs)
    if not ok or src is None or dist is None:
        return False

    shutil.copy(src, dist)
    return True


def move(*args, **kwargs) -> bool:
    ok, src, dist = __ready_move(*args, **kwargs)
    if not ok or src is None or dist is None:
        return False

    shutil.move(str(src), dist)
    return True