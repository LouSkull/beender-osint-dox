import os
from helper import printer, timer
import time
import subprocess


class Scan:
    @timer.timer
    def __init__(self):
        if os.name == "nt":
            printer.info("Windows system detected..! Doing a netsh scan...")
            time.sleep(1)
            try:
                subprocess.run(["netsh", "wlan", "show", "networks"], check=True)
            except subprocess.CalledProcessError as e:
                printer.error(f"Error : {e.returncode}")
        else:
            printer.info("Linux system detected..! Doing a nmcli scan...")
            time.sleep(1)
            try:
                subprocess.run(["nmcli", "dev", "wifi"], check=True)
            except subprocess.CalledProcessError as e:
                printer.error(f"Error : {e.returncode}")
