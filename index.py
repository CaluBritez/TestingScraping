import requests
from bs4 import BeautifulSoup

url = "https://www.forbes.com/sites/michelecatalano/2013/01/24/7-websites-for-music-lovers/?sh=78ee6cfa2e3c"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a')
    
    for link in links:
        print(link.get('href'))
else:
    print("Error al acceder a la página:", response.status_code)