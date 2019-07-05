#!/usr/bin/env python3

import asyncio
from flipdotapi import remote_sign as sign
from datetime import datetime

import time

import configparser
import logging

from os import path
import sys

async def clock():
    while True:
        new_time = time.strftime(time_format)
        if new_time != old_time:
                logging.debug(new_time)
                sign.write_text(new_time, alignment="centre",
                                font_name=display_font, fit=True)

async def main():
    res = await asyncio.gather(clock())
    return res

if __name__ == "__main__":

    formatter = "[%(asctime)s] :: %(levelname)s :: %(name)s :: %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=formatter)
    logger = logging.getLogger(__name__)

    config = configparser.ConfigParser()
    config_file = 'config.ini'
    if path.exists(config_file):
        config.read(config_file)
    else:
        logging.error("Config file missing: {}".format(config_file))
        sys.exit(1)

    sign_url = config.get('FLIPDOT_SERVER', 'URL')
    sign_columns = config.getint('FLIPDOT_SERVER', 'COLUMNS')
    sign_rows = config.getint('FLIPDOT_SERVER', 'ROWS')
    sign_sim = config.getboolean('FLIPDOT_SERVER', 'SIMULATOR')
    sign = sign(sign_url, sign_columns, sign_rows, simulator=sign_sim)

    display_font = config.get('DISPLAY', 'FONT')

    time_format = "%I:%M" #config.get('DISPLAY', 'CLOCK_PATTERN')

    

    old_time = time.strftime(time_format)
    
    clock1 = asyncio.run(main())
    print()
    print(f"clock: {clock1}")
