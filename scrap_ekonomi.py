import newspaper
from time import sleep
from newspaper import Article
import nltk
import csv
import requests
nltk.download('punkt')
from bs4 import BeautifulSoup
import pandas as pd


list1 = []
list2 = []
lista = []
listb = []

response = requests.get("https://www.haberler.com/saglik/")
sleep(3)
html_category_links = response.text
soupie = BeautifulSoup(html_category_links, "html.parser")
tags = soupie.find_all(name="a", class_="boxStyle color-general hbBoxMainText")
article_links = []

for tag in tags:

    link = tag.get("href")
    article_links.append(link)

if bool(article_links):
    for links in article_links:

        splitlinks = links.split(",")

        mylink=f"{'http://haberler.com'+(splitlinks[0])}"
        sleep(2)
        resp = requests.get(mylink)
        sleep(2)
        haber = resp.text
        soup = BeautifulSoup(haber, "html.parser")

        a = soup.select_one('h2[class^=hbptHead_h2]').text

        if a ==" Sağlık Haberleri ":
            list1.append(a)
            b=soup.find(name="main",class_="hbptContent haber_metni")

            mytxt =""
            for p in b.find_all("p"):
                mytxt += ' '+p.getText()

            list2.append(mytxt)
            data = {"Kategori":list1, "Metin": list2}
            df = pd.DataFrame(data)
            print(df)
            df.to_csv("saglik.csv")









