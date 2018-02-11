import requests
from bs4 import BeautifulSoup
import selenium  
from selenium import webdriver
book = (input("enter the book u want :"))
page = 1
num = 1
books = []
links = []
baseurl = "http://www.ebook777.com/page/"

while page <3:
    url = baseurl + str(page) + "/?s=" + book
    print(url)
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    
    for bookname in soup.findAll('a', attrs={'class':'title'}):
        books.append(bookname.text)
    
    for link in soup.findAll('a', attrs={'class':'title'}):
        links.append(link.get('href','/n''/n'))
    
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
download_url = links[download_book]
print(download_url)
download = requests.get(download_url).text
download_soup = BeautifulSoup(download,'html.parser')
spans = download_soup.find_all('span',attrs={'class':'download-links'})
for span in spans:
    downloads = span.find_all('a')
    fine = []
    for download in downloads:
        fine.append(download['href'])
        print(fine[0])
url = fine[0]
driver = webdriver.Chrome()
driver.get(url)
        
         
        
        

                
