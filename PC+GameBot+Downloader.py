
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
import selenium  
from selenium import webdriver

game = (input("enter the book u want :"))
page = 1
books = []
links = []
game = (input("enter the book u want :"))
baseurl = "http://gamestorrent.co/?s="
# number of pages to extract 
while page <1:
    url = baseurl + game
    print(url)
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    spans = soup.find_all('h2',attrs={'class':'title'})
    for bookname in spans:
        books.append(bookname.text)

    links = []
    for link in spans:
        downloads = link.find_all('a',attrs={'rel':'bookmark'})
        for download in downloads:
            links.append(download['href'])
            
    page+=1

n = 0
nu = 0
for boo in books:
    print(n ,boo)
    n+=1
for li in links:
    print(nu ,li)
nu+=1   

download_book = int(input("enter the book number:"))
print(links[download_book])
url = links[download_book]
driver = webdriver.Chrome()
driver.get(url)

