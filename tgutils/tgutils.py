#!/usr/bin/env python
# ------------------------------------------------------------------
# TGUtils - a collection of tools and utils for my scripts
#           copyleft 2023-2025 Transgirl
# ------------------------------------------------------------------
import os


# ---------------------------------------------------------------------- colors
class Colors:
    reset     = "\033[0m"
    black     = "\033[0;30m"
    red       = "\033[0;31m"
    green     = "\033[0;32m"
    yellow    = "\033[0;33m"
    blue      = "\033[0;34m"
    purple    = "\033[0;35m"
    cyan      = "\033[0;36m"
    white     = "\033[0;37m"
    gray      = "\033[1;30m"
    italic    = "\033[0;3m"
    bold      = "\033[0;1m"
    faint     = "\033[2m"
    underline = "\033[4m"
    crossed   = "\033[9m"

    colors = [
            ('%R', reset),
            ('%B', bold),
            ('%F', faint),
            ('%U', underline),
            ('%C', crossed),
            ('%r', red),
            ('%g', green),
            ('%y', yellow),
            ('%p', purple),
            ('%b', blue),
            ('%c', cyan),
            ('%w', white),
            ('%i', italic)
    ]

# --------------------------------------------------------------------- TGUtils
class TGUtils:
    def __init__(self):
        pass

    def colorize(self, message, remove=False):
        for color in Colors.colors:
            repl = '' if remove else color[1]
            message = message.replace(color[0], repl)
        return message

    def printf(self, message, remove=False, nl=False):
        end = '\n\n' if nl else '\n'
        print(self.colorize(message, remove=remove), end=end)

    def cprint(self, message, remove=False, nl=False):
        temp = self.colorize(message, remove=True)
        width = (os.get_terminal_size().columns - len(temp)) // 2
        spcs = width * ' '
        self.printf(f"{spcs}{message}", remove=remove, nl=nl)
