from argparse import ArgumentParser, REMAINDER

from imagenate.libs.enum import CustomEnum


class Command(CustomEnum):
    COPY = "copy"


def create_base_argperser() -> ArgumentParser:
    argparser = ArgumentParser()
    argparser.description = "file manager"
    argparser.add_argument("command", type=str, choices=Command.get_values())
    argparser.add_argument(
        "help",
        type=str,
        choices=(
            "",
            "help",
        ),
        default="",
        nargs="?",
    )

    return argparser


def create_check_help_argperser() -> ArgumentParser:
    argparser = create_base_argperser()
    argparser.add_argument(
        "help",
        type=str,
        choices=(
            "",
            "help",
        ),
        default="",
        nargs="?",
    )
    argparser.add_argument(
        "other",
        type=str,
        default="",
        nargs=REMAINDER,
    )

    return argparser
