__author__ = 'MAWood'
import threading
import os

import pygameui as ui
import Screens.Load as Load
import DataReader
import Screens.Action as Action
import Screens.Storage as Storage
import Globals


ba1 = 'Load'
ba2 = 'Storage'
ba3 = 'Action'
ba4 = ''


class Home(ui.Scene):
    def __init__(self):
        ui.Scene.__init__(self)

        # proc = subprocess.Popen('ping -c 1 192.168.1.176 | grep 'packets transmitted' |  cut -c 24', stdout=subprocess.PIPE)
        # tmp = proc.stdout.read()
        tmp = int(os.popen("ping -c 1 192.168.1.176 | grep 'packets transmitted' |  cut -c 24").read())
        self.ba1_button = ui.Button(ui.Rect(Globals.MARGIN, Globals.MARGIN, 130, 90), ba1)
        self.ba1_button.on_clicked.connect(self.button_handler)
        self.add_child(self.ba1_button)

        self.ba2_button = ui.Button(ui.Rect(170, Globals.MARGIN, 130, 90), ba2)
        self.ba2_button.on_clicked.connect(self.button_handler)
        self.add_child(self.ba2_button)

        self.ba3_button = ui.Button(ui.Rect(Globals.MARGIN, 130, 130, 90), ba3)
        self.ba3_button.on_clicked.connect(self.button_handler)
        self.add_child(self.ba3_button)

        self.ba4_button = ui.Button(ui.Rect(170, 130, 130, 90), ba4)
        self.ba4_button.on_clicked.connect(self.button_handler)
        self.add_child(self.ba4_button)

    def button_handler(self, btn, mbtn):
        if btn.text == ba1:
            load = Load.Load()
            datareader = DataReader.DataReader(load)
            threading.Thread(target=datareader).stop()
            threading.Thread(target=datareader).start()
            ui.scene.push(load)
        elif btn.text == ba2:
            ui.scene.push(Storage.Storage())
            # alert = ui.alert.AlertView('Test', 'This is an alert')
            #ui.scene.push(alert)
            # alert.show_alert('Hi')
        elif btn.text == ba3:
            ui.scene.push(Action.Action())