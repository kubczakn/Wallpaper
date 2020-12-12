import ctypes
import os
import random
import sched, time

SPI_SETDESKWALLPAPER = 20

path = "C:/Users/natha/Documents/Wallpapers/"
dirs = os.listdir(path)

dirs = [path + file for file in dirs]

s = sched.scheduler(time.time, time.sleep)


def wallpaper(sc):
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, random.choice(dirs), 3)
    s.enter(3600, 1, wallpaper, (s,))


s.enter(3600, 1, wallpaper, (s,))
s.run()
