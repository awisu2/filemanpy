from pathlib import Path

a = Path("a")
b = a / "b"
ba = b / "a"
bb = b / "b"
bba = bb / "a"
c = a / "c"


def relative(a: Path, b: Path):
    try:
        print(a.relative_to(b))
    except Exception as e:
        print("error {}".format(e))


relative(a, bba)
relative(bba, a)
relative(ba, bb)
print([1] + [2, 3])


print("----------")
src = Path("src")
for path in src.glob("*/"):
    print(path)

print("----------")
src = Path("src")
for path in src.glob("**/*"):
    rel = path.relative_to(src)

    dirs = []
    path = rel
    while True:
        path = path.parent
        if path == Path("."):
            break
        dirs.append(path.name)
    d = "_".join(dirs)
    print(rel, ":" + d)

    if rel.exists():
        for dir in rel.iterdir():
            print(dir, type(dir))


print("----------")
path01 = Path("a/b")
path02 = Path("c/d")
path_join = path01 / path02
print(path_join)
