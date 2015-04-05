__author__ = 'MAWood'
import pygame
import os
import pygameui as ui
import logging
import commands
from sys import exit

log_format = '%(asctime)-6s: %(name)s - %(levelname)s - %(message)s'
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(log_format))
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)

os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

MARGIN = 20

ba1 = 'Load'
ba2 = 'Storage'

# class Button():
#    def __init__(text, x1, y1, x2, y2)
#	self.button = ui.Button

class Home(ui.Scene):
    def __init__(self):
        ui.Scene.__init__(self)

        output = commands.getstatusoutput('git pull')
        logger.info(output)
        if output != 'Already up-to-date.':
            commands.getstatusoutput('(sleep 5; sudo python ServerMonitor.py)&')
            exit()

        self.ba1_button = ui.Button(ui.Rect(MARGIN, MARGIN, 130, 90), ba1)
        self.ba1_button.on_clicked.connect(self.button_handler)
        self.add_child(self.ba1_button)

        self.ba2_button = ui.Button(ui.Rect(170, MARGIN, 130, 90), ba2)
        self.ba2_button.on_clicked.connect(self.button_handler)
        self.add_child(self.ba2_button)

    def button_handler(self, btn, mbtn):
        logger.info(btn.text)

        if btn.text == ba1:
            ui.scene.push(Load())
        elif btn.text == ba2:
            ui.scene.push(Storage())

class Load(ui.Scene):
    def __init__(self):
        ui.Scene.__init__(self)

        self.ba1_button = ui.Button(ui.Rect(MARGIN, MARGIN, 280, 200), 'Back')
        self.ba1_button.on_clicked.connect(self.button_handler)
        self.add_child(self.ba1_button)


    def button_handler(self, btn, mbtn):
        logger.info(btn.text)
        ui.scene.pop()

class Storage(ui.Scene):
    def __init__(self):
        ui.Scene.__init__(self)


    def button_handler(self, btn, mbtn):
        logger.info(btn.text)
        ui.scene.pop()

ui.init('Raspberry Pi UI', (320, 240))
pygame.mouse.set_visible(False)
ui.scene.push(Home())
ui.run()
