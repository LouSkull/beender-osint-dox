from colorama import Fore, Style


def print_colored(message, color, prefix, *args, **kwargs):
    print(f"{color}{prefix} {message}{Style.RESET_ALL}", *args, **kwargs)


def info(message, *args, **kwargs):
    print_colored(message, Fore.GREEN, "[>]", *args, **kwargs)


def success(message, *args, **kwargs):
    print_colored(message, Fore.GREEN, "[>]", *args, **kwargs)


def error(message, *args, **kwargs):
    print_colored(message, Fore.GREEN, "[>]", *args, **kwargs)


def warning(message, *args, **kwargs):
    print_colored(message, Fore.GREEN, "[>]", *args, **kwargs)


def debug(message, *args, **kwargs):
    print_colored(message, Fore.GREEN, "[>]", *args, **kwargs)


def nonprefix(message, *args, **kwargs):
    print(message, *args, **kwargs)
