import ctypes

## Path
SPI_SETDESKWALLPAPER = 20

def changeWP():
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, "absolute path", 0)
