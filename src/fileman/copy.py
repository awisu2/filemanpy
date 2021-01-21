from pathlib import Path
import shutil


def copy(src, dist):
    _src = Path(src)
    _dist = Path(dist)

    shutil.copy(_src, _dist)
