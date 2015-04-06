__author__ = 'MAWood'
import os
import time

import Globals


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
        while not (self.terminated or Globals.TERMINATING):
            # Read channel 0 in single-ended mode using the settings above
            self.update_info()
            self.scene.update_cpu(self.cpu_load)
            self.scene.update_mem(self.mem_free, self.mem_total)
            time.sleep(Globals.UPDATE_DELAY)

    def update_info(self):
        self.on = bool(os.popen(Globals.ON_COMMAND).read())
        if self.on:
            self.cpu_load = os.popen("ssh " + Globals.USERNAME + "@" + Globals.HOST + Globals.CPU_LOAD_COMMAND).read()
            Globals.LOGGER.info(self.cpu_load)
            self.cpu_load = float(self.cpu_load) * Globals.CPU_LOAD_COEFFICIENT
            self.mem_total = int(os.popen(
                "ssh " + Globals.USERNAME + "@" + Globals.HOST + Globals.MEM_TOTAL_COMMAND).read()) * Globals.MEM_TOTAL_COEFFICIENT
            self.mem_free = int(
                os.popen("ssh " + Globals.USERNAME + "@" + Globals.HOST + Globals.MEM_FREE_COMMAND).read())
            self.mem_free += int(
                os.popen("ssh " + Globals.USERNAME + "@" + Globals.HOST + Globals.MEM_BUFFERS_COMMAND).read())
            self.mem_free += int(
                os.popen("ssh " + Globals.USERNAME + "@" + Globals.HOST + Globals.MEM_CACHED_COMMAND).read())
            self.mem_free *= Globals.MEM_FREE_COEFFICIENT
        else:
            self.cpu_load = 0.0
            self.mem_total = 0
            self.mem_free = 0
