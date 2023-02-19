"""Я тут из-за pylint"""
import re
from time import sleep
import csv
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":
           "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) "
           "Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"}

with open('Goods_Sulpak.csv', 'w', encoding='utf-8', newline='') as fil:
    writer = csv.writer(fil)
    writer.writerow((
        "Наименование и арттикул",
        "Стоимость",
        "Наличие",
        "Изображение"
    ))

for count in range(1, 2):
    sleep(1)
    url = f"https://vsem-darom.ru/promo-actions?p={count}"
    response = requests.get(url, headers, timeout=10)
    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find_all("div", class_="pc")
    for i in data:
        sleep(0.1)
        name = i.find("div", class_="pc-name").text
        price = i.find("span").text
        stock = i.find("div", class_="pc-availability").text
        image_str = i.find("div", class_="pc-image")
        result = re.split(r'"', str(image_str))
        image = "https://vsem-darom.ru" +result[7]
        with open('Goods_Sulpak.csv', 'a', encoding='utf-8', newline='') as fil:
            writer = csv.writer(fil)
            writer.writerow((
                name,
                price,
                stock,
                image
            ))

        print(name)
        print(price)
        print(stock)
        print(image)
