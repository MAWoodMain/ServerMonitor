__author__ = 'MAWood'

import pygameui as ui
import Globals


class Load(ui.Scene):
    def __init__(self):
        ui.Scene.__init__(self)

        # self.ba1_button = ui.Button(ui.Rect(MARGIN, MARGIN, 280, 200), 'Back')
        #self.ba1_button.on_clicked.connect(self.button_handler)
        #self.add_child(self.ba1_button)


        self.cpu_view = ui.ProgressView(ui.Rect(Globals.MARGIN, 100, 280, 40))
        self.add_child(self.cpu_view)

        self.mem_view = ui.ProgressView(ui.Rect(Globals.MARGIN, 200, 280, 40))
        self.add_child(self.mem_view)

    def update_cpu(self, load):
        self.cpu_view.progress = load

    def update_mem(self, free, total):
        if total != 0:
            self.mem_view.progress = 1 - (free / total)
        else:
            self.mem_view.progress = 0

    def button_handler(self, btn, mbtn):
        ui.scene.pop()