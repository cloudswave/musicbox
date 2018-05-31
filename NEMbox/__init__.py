#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
网易云音乐 Entry
'''
from __future__ import (
    print_function, unicode_literals, division, absolute_import
)
import curses
import traceback
import argparse
import sys

from future.builtins import str

from .menu import Menu

version = '0.2.4.3'


def start():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v",
                        "--version",
                        help="show this version and exit",
                        action="store_true")
    parser.add_argument('-c','--cmd', type=str, help = '启动时传入的指令，如："?":自动随机播放，"0,0,1":自动播放新歌榜')
    args = parser.parse_args()
    if args.version:
        latest = Menu().check_version()
        curses.endwin()
        print('NetEase-MusicBox installed version:' + version)
        if latest != version:
            print('NetEase-MusicBox latest version:' + str(latest))
        sys.exit()

    ords = []
    if args.cmd:
        ords = args.cmd.split(',')
        print('cmd:', ords)
    nembox_menu = Menu()
    try:
        nembox_menu.start_fork(version, ords)
    except (OSError, TypeError, ValueError, KeyError):
        # clean up terminal while failed
        nembox_menu.screen.keypad(1)
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        traceback.print_exc()


if __name__ == '__main__':
    start()
