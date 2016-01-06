# -*- coding: utf-8 -*-

from time import sleep
from StringIO import StringIO

import requests
from bs4 import BeautifulSoup
import Image

site = "http://www.douyutv.com"
url = "http://www.douyutv.com/directory"

r = requests.get(url)
r.encoding = 'utf-8'
html = r.content

soup = BeautifulSoup(html, "lxml") 
g_list = soup.find_all(name="li", attrs={"class": "unit"})

for game in g_list:
    print game.find_all(name="p", attrs={"class": "title"})[0].text
    print site + game.find_all(name="a")[0].get("href")
    print game.find_all(name="img")[0].get('data-original')

game_name = []
game_value_list = []

for game in g_list:
    game_name.append(game.find_all(name="p", attrs={"class": "title"})[0].text)
    game_room = site + game.find_all(name="a")[0].get("href")
    game_pic = game.find_all(name="img")[0].get('data-original')
    game_value = {
        "room": game_room,
         "picture": game_pic
    }
    game_value_list.append(game_value)
    
# game_info 为字典对象，key是游戏名，value是由游戏房间地址room和游戏图片地址picture组成的字典对象
# 即game_info为值为字典对象的字典对象
game_info = dict(zip(game_name, game_value_list))