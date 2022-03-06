from attr import attrs
import bs4
from bs4 import BeautifulSoup
import requests



artists = input("Enter the name of the artist : ")

url = requests.get("https://www.goodreads.com/search?q="+ artists + "&qid=")

data_a = BeautifulSoup(url.text , 'html.parser')

data_b = data_a.find('div' , attrs={'div' , 'leftContainer'})

data_c = data_b.find_all('a' , attrs={'class' : 'bookTitle'})

j=1
for i in data_c :
    print(f"{j} : {i.text}" , end="\n")
    j+=1

#print(url)