import selenium
import requests
import shutil
import ctypes
import os
import random
from selenium import webdriver


def download_imgs():
    DRIVER_PATH = "C:/Users/natha/Desktop/Scraping/chromedriver"
    wd = webdriver.Chrome(executable_path=DRIVER_PATH)

    search_url = "https://www.pexels.com/search/nature%20wallpaper/"
    wd.get(search_url)

    images = wd.find_elements_by_class_name("js-download")
    for image in images:
        print(image.get_attribute('href'))


SPI_SETDESKWALLPAPER = 20

path = "C:/Users/natha/Documents/Wallpapers/"
dirs = os.listdir(path)

dirs = [path + file for file in dirs]


def wallpaper():
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, random.choice(dirs), 3)


#download_imgs()
wallpaper()
