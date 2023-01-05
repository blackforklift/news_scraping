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

response = requests.get("https://www.haberler.com/spor/")
sleep(3)
html_category_links = response.text
soupie = BeautifulSoup(html_category_links, "html.parser")
tags = soupie.find_all(name="a", class_="box boxStyle hbBoxMainText color-sport")
article_links = []

for tag in tags:

    link = tag.get("href")
    article_links.append(link)

if bool(article_links):
    for links in article_links:

        splitlinks = links.split(",")

        mylink = f"{splitlinks[0]}"
        sleep(2)
        resp = requests.get(f"{splitlinks[0]}")
        sleep(2)
        haber = resp.text
        soup = BeautifulSoup(haber, "html.parser")

        a = soup.select_one('h2[class^=hbptHead_h2]').text

        if a ==" Spor Haberleri ":
            list1.append(a)
            b=soup.find(name="main",class_="hbptContent haber_metni")

            mytxt =""
            for p in b.find_all("p"):
                mytxt += ' '+p.getText()

            list2.append(mytxt)
            data = {"Kategori":list1, "Metin": list2}
            df = pd.DataFrame(data)

response2 = requests.get("https://www.haberler.com/spor/futbol")
sleep(3)
html_category_links2 = response2.text
soupie2 = BeautifulSoup(html_category_links2, "html.parser")
tags2 = soupie2.find_all(name="a", class_="box boxStyle hbBoxMainText color-sport")
article_links2 = []

for tag2 in tags2:

    link2 = tag2.get("href")
    article_links2.append(link2)

if bool(article_links2):
    for links in article_links2:

        splitlinks2 = links.split(",")

        mylink2 = f"{splitlinks2[0]}"
        sleep(2)
        resp2 = requests.get(f"{splitlinks2[0]}")
        sleep(2)
        habe2r = resp2.text
        soup = BeautifulSoup(habe2r, "html.parser")

        a2 = soup.select_one('h2[class^=hbptHead_h2]').text


        lista.append(a2)
        b2=soup.find(name="main",class_="hbptContent haber_metni")

        mytxt2 =""
        for p in b2.find_all("p"):
            mytxt2 += ' '+p.getText()

        listb.append(mytxt2)
        data2 = {"Kategori":lista, "Metin":listb}
        df2=pd.DataFrame(data2)
        print(df2)
        a3= pd.concat([df,df2])
        print(a3)
        a3.to_csv("spor2.csv")








