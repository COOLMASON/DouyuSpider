# -*- coding: utf-8 -*-

from time import sleep
from StringIO import StringIO

import requests
from bs4 import BeautifulSoup
import Image


def main():
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
    game_room = []
    game_pic = []
    game_value_list = []

    for game in g_list:
        game_name.append(game.find_all(name="p", attrs={"class": "title"})[0].text)
        
        tempr = site + game.find_all(name="a")[0].get("href")
        game_room.append(tempr)
        
        tempp = game.find_all(name="img")[0].get('data-original')
        game_pic.append(tempp)
        
        game_value = {
            "room": tempr,
             "picture": tempp
        }
        
        game_value_list.append(game_value)

    # game_info 为字典对象，key是游戏名，value是由游戏房间地址room和游戏图片地址picture组成的字典对象
    # 即game_info为值为字典对象的字典对象
    game_info = dict(zip(game_name, game_value_list))
    imgsrcs = dict(zip(game_name, game_pic))

    return  imgsrcs


# 图片保存
def save_imgs(imgs):
    print '\n'
    print u'开始保存图片...'
    sleep(2)

    for imgname, imgsrc in imgs.items():
        bin_content = requests.get(imgsrc).content
        img = Image.open(StringIO(bin_content))
        img.save(imgname+".jpg")
        print imgname + ' saved.'
        sleep(0.5)

    print u'所有图片保存完成!!'


if __name__ == '__main__':
    imgsrcs = main()
    save_imgs(imgsrcs)