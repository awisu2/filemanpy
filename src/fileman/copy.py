from pathlib import Path
import shutil


def copy(src: str, dist: str):
    _src = Path(src)
    _dist = Path(dist)

    shutil.copy(_src, _dist)
