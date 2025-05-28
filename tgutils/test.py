#!/usr/bin/env python
from tgutils import TGUtils


class Test(TGUtils):
    def __init__(self):
        super().__init__()

    def run(self):
        self.cprint('%cHello world...%R')


if __name__ == '__main__':
    app = Test()
    app.run()
