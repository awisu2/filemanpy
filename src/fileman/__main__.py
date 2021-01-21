from .main.share import create_base_argperser, Command

from .main.copy import copy

# from .main.concat import concat, concat_dir
# from .main.info import info
# from .main.resize import resize


def main():
    """コマンド呼び出し"""
    args, _ = create_base_argperser().parse_known_args()
    command = Command(args.command)

    if command == Command.COPY:
        copy()


if __name__ == "__main__":
    main()
