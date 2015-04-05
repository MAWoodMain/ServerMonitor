__author__ = 'MAWood'

import pygameui as ui


class Storage(ui.Scene):
    def __init__(self):
        ui.Scene.__init__(self)


    def button_handler(self, btn, mbtn):
        ui.scene.pop()