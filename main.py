#!/usr/bin/env python

import os

from echis_web import create_app

if __name__ == '__main__':
    create_app("dev").run()
