__author__ = 'MAWood'

import os
import logging
import signal
import sys

import pygame
import pygameui as ui
import Screens.Home as Home
import Globals






# Configure logging
log_format = '%(asctime)-6s: %(name)s - %(levelname)s - %(message)s'
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(log_format))
Globals.LOGGER = logging.getLogger()
Globals.LOGGER.setLevel(logging.DEBUG)
Globals.LOGGER.addHandler(console_handler)

# Configure screen
os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

# Configure UI
ui.init('Raspberry Pi UI', (320, 240))
pygame.mouse.set_visible(False)



def signal_handler(signal, frame):
    Globals.TERMINATING = True
    print('You pressed Ctrl+C!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

home = Home.Home()
ui.scene.push(home)
ui.run()
