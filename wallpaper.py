import selenium
import requests
import uuid
import ctypes
import os
import random
from selenium import webdriver


def get_links():
    DRIVER_PATH = "C:/Users/natha/Desktop/Scraping/chromedriver"
    wd = webdriver.Chrome(executable_path=DRIVER_PATH)

    search_url = "https://www.pexels.com/search/nature%20wallpaper/"
    wd.get(search_url)
    images = wd.find_elements_by_class_name('js-download')
    links = []
    for image in images:
        link = image.get_attribute('href')
        links.insert(0, link)

    return links


def download_images(dest, links):
    for link in links:
        file = requests.get(link)
        name = str(uuid.uuid4())
        path = dest + name + '.jpg'
        with open(path, 'wb') as f:
            f.write(file.content)


def wallpaper(path):
    SPI_SETDESKWALLPAPER = 20
    dirs = os.listdir(path)
    dirs = [path + file for file in dirs]
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, random.choice(dirs), 3)


abs_path = "C:/Users/natha/Documents/Wallpapers/"


#download_images(abs_path, get_links())
wallpaper(abs_path)
