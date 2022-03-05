
import imp
from bs4 import BeautifulSoup
import requests 
import bs4 
#==========================================================
#                       Goodreads
#==========================================================


def goodreads(artist) :

    url = requests.get("https://www.goodreads.com/search?q="+ artist + "&qid=")

    data_a = BeautifulSoup(url.text , 'html.parser')

    data_b = data_a.find('div' , attrs={'div' , 'leftContainer'})

    data_c = data_b.find_all('a' , attrs={'class' : 'bookTitle'})

    for i in data_c :
         print("Book name : " + i.text)
     

#==========================================================
#                       wikipedia
#==========================================================


ListOfWriters = []

Choice = input("Enter the Letter you want for writer : ")
Choice = Choice.upper()

page = requests.get("https://en.m.wikipedia.org/wiki/List_of_authors_by_name:_A")

soup = bs4.BeautifulSoup(page.content)

names = soup.findAll()

for name in names :
    if name.string == None :
        continue
    elif name.string[0] == Choice and len(name.string) > 1 :
        print("Writer name : " + name.string)
        ListOfWriters.append(name.string)

artist = input("Enter your choice : ")
if artist not in ListOfWriters :
    print("Wrong name ! ")
else :
    goodreads(artist)
    
