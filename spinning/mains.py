# encoding=utf8

from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals
from future.standard_library import install_aliases
install_aliases()
import sys
import time
import argparse
import codecs
import blessings

# MAIN

t = blessings.Terminal()

class spin:
    def __init__(self, sec=5):
        def spin():
            while True:
                p = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
                for x in p:
                    yield t.cyan(x)

        spinner = spin()
        for _ in range(sec*10):
            sys.stdout.write(next(spinner))
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write('\b')
