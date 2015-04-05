__author__ = 'MAWood'

HOST = "192.168.1.176"
USERNAME = "mawood"

ON_COMMAND = "ping -c 1 192.168.1.176 | grep 'packets transmitted' |  cut -c 24"

CPU_LOAD_COMMAND = "cat /proc/loadavg | cut -c 1-4"
CPU_LOAD_COEFFICIENT = 0.125

MEM_TOTAL_COMMAND = "cat /proc/meminfo | grep MemTotal | cut -c 10-24 | sed 's/ //g'"
MEM_TOTAL_COEFFICIENT = 1.0

MEM_FREE_COMMAND = "cat /proc/meminfo | grep MemFree | cut -c 10-24 | sed s/ //g"
MEM_FREE_COEFFICIENT = 1.0

import pygame
import os
import time
import pygameui as ui
import logging
import subprocess
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

class DataReader():
    def __init__(self, scene):
        self.scene = scene
        self.terminated = False

        self.on = False
        self.cpu_load = 0.0
        self.mem_total = 0
        self.mem_free = 0

    def terminate(self):
        self.terminated = True

    def __call__(self):
        while not self.terminated:
            # Read channel 0 in single-ended mode using the settings above
            self.update_info()
            self.scene.update_cpu(self.cpu_load)
            self.scene.update_mem(self.mem_free, self.mem_total)
            time.sleep(2)

    def update_info(self):
        self.on = bool(os.popen(ON_COMMAND).read())
        if self.on:
            self.cpu_load = float(os.popen("ssh " + USERNAME + "@" + HOST + " " + CPU_LOAD_COMMAND).read()) *CPU_LOAD_COEFFICIENT
            self.mem_total = int(os.popen("ssh " + USERNAME + "@" + HOST + " " + MEM_TOTAL_COMMAND).read()) *MEM_TOTAL_COEFFICIENT
            self.mem_free = int(os.popen("ssh " + USERNAME + "@" + HOST + " " + MEM_FREE_COMMAND).read()) *MEM_FREE_COEFFICIENT
        else:
            self.cpu_load = 0.0
            self.mem_total = 0
            self.mem_free = 0

class Home(ui.Scene):
    def __init__(self):
        ui.Scene.__init__(self)

        #proc = subprocess.Popen('ping -c 1 192.168.1.176 | grep 'packets transmitted' |  cut -c 24', stdout=subprocess.PIPE)
        #tmp = proc.stdout.read()
        tmp = int(os.popen("ping -c 1 192.168.1.176 | grep 'packets transmitted' |  cut -c 24").read())
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

        self.cpu_view = ui.ProgressView(ui.Rect(MARGIN, 200, 280, 40))
        self.add_child(self.progress_view)

    def update_cpu(self, load):
        self.cpu_view.progress(load)

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
