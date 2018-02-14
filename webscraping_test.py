"""
Sample example for knowing how to use BeutufulSoup library 
for WebScraping
"""


import requests
from bs4 import BeautifulSoup

r = requests.get("https://pythonhow.com/example.html")
c = r.content

soup = BeautifulSoup(c, "html.parser")
all_cls = soup.find_all("div", {"class": "cities"})

print(all_cls[0].find_all("h2")[0].text)

for item in all_cls:
    print(item.find_all("h2")[0].text)
for item in all_cls:
    print(item.find_all("p")[0].text)

    
    
