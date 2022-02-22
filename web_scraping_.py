from re import search
from markupsafe import string
import requests 
import bs4
#==========================================================
#                       MAIN
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

search = input("Enter the name of the writer you want : ")

if search in ListOfWriters :
    print("It's available ! ")
else :
    print("It's not available ! ")