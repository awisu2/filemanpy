from argparse import ArgumentParser

from imagenate.libs.enum import CustomEnum


class Command(CustomEnum):
    COPY = "copy"


def create_base_argperser() -> ArgumentParser:
    argparser = ArgumentParser()
    argparser.description = "file manager"
    argparser.add_argument("command", type=str, choices=Command.get_values())
    return argparser
