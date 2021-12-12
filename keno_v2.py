from bs4 import BeautifulSoup
from selenium import webdriver
import time
import random
import pandas as pd
from datetime import datetime
from pandas import ExcelWriter
import requests


headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
}

url = 'https://www.stoloto.ru/keno/archive?from=24.06.2020&to=24.06.2020&firstDraw=24.06.&lastDraw=251057&mode=date'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

games = soup.find_all('div', class_='elem')
print(len(games))