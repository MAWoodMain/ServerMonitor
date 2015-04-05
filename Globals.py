__author__ = 'MAWood'

MARGIN = 20

HOST = "192.168.1.176"
USERNAME = "mawood"

UPDATE_DELAY = 0

ON_COMMAND = "ping -c 1 192.168.1.176 | grep 'packets transmitted' |  cut -c 24"

CPU_LOAD_COMMAND = " \"cat /proc/loadavg\" | cut -c 1-4"
CPU_LOAD_COEFFICIENT = 0.125

MEM_TOTAL_COMMAND = " \"grep MemTotal /proc/meminfo\" | awk '{print $2}'"
MEM_TOTAL_COEFFICIENT = 1.0

MEM_FREE_COMMAND = " \"grep MemFree /proc/meminfo\" | awk '{print $2}'"
MEM_BUFFERS_COMMAND = " \"grep Buffers /proc/meminfo\" | awk '{print $2}'"
MEM_CACHED_COMMAND = " \"grep Cached /proc/meminfo\" | awk '{print $2}' | head -1"
MEM_FREE_COEFFICIENT = 1.0

LOGGER = ""

TERMINATING = False