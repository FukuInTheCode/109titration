from src.help.display_help import display_help


def check_argv(argv: list[str]) -> int:
    if len(argv) != 2:
        exit(84)
    if argv[1] == "-h":
        return display_help()
