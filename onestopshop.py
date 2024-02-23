import requests
from bs4 import BeautifulSoup

url = 'https://echo.uib.no/arrangement/genvors-2'

response = requests.get(url)   

#find href = "/auth/logg-inn"

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    loginn = soup.find_all('a', href=True)
    for link in loginn:
        if link['href'] == "/auth/logg-inn":
            #press the link
    print(soup.prettify())
