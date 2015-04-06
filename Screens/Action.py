__author__ = 'MAWood'
import os

import Globals
import pygameui as ui


b1 = "Suspend server"
b2 = "Awaken server"
b3 = "Restart server"
b4 = "Shutdown server"


class Action(ui.Scene):
    def __init__(self):
        self.b1_button = ui.Button(ui.Rect(Globals.MARGIN, Globals.MARGIN, 130, 90), b1)
        self.b1_button.on_clicked.connect(self.button_handler)
        self.add_child(self.b1_button)

        self.b2_button = ui.Button(ui.Rect(170, Globals.MARGIN, 130, 90), b2)
        self.b2_button.on_clicked.connect(self.button_handler)
        self.add_child(self.b2_button)

        self.b3_button = ui.Button(ui.Rect(Globals.MARGIN, 130, 130, 90), b3)
        self.b3_button.on_clicked.connect(self.button_handler)
        self.add_child(self.b3_button)

        self.b4_button = ui.Button(ui.Rect(170, 130, 130, 90), b4)
        self.b4_button.on_clicked.connect(self.button_handler)
        self.add_child(self.b4_button)

    def button_handler(self, btn, mbtn):
        if btn.text == b1:
            os.popen('sudo pm-suspend')
        elif btn.text == b2:
            os.popen('')
        elif btn.text == b3:
            os.popen('sudo reboot')
        elif btn.text == b4:
            os.popen('')