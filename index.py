import requests
from bs4 import BeautifulSoup
import json

url = "https://www.forbes.com/sites/michelecatalano/2013/01/24/7-websites-for-music-lovers/?sh=78ee6cfa2e3c"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a')
    lista_links = []
    
    for link in links:
        #print(link.get('href'))
        lista_links.append(link.get('href'))
else:
    print("Error al acceder a la página:", response.status_code)

def verificar_url(string):
    if string and (string.startswith("http://") or string.startswith("https://")) and "forbes" not in string and string != None:
        return True
    return False

links_clean = list(filter(verificar_url,lista_links))
print(links_clean)


def obtener_datos(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Encuentra todas las etiquetas <h1> y <p> y las convierte a cadenas de texto
            h1_tags = [str(tag) for tag in soup.find_all('h1')]
            p_tags = [str(tag) for tag in soup.find_all('p')]
            return h1_tags + p_tags  # Concatena las listas de etiquetas h1 y p
    except Exception as e:
        print("Error al obtener datos de", url)
        print(e)
    return []

def crear_diccionario(lista):
    datos_diccionario = {}
    for url in lista:
        datos = obtener_datos(url)
        datos_diccionario[url] = datos
    return datos_diccionario

#Obtenemos diccionario en formato json como lo pide la consigna
datos = crear_diccionario(links_clean)
diccionario_json = json.dumps(datos)

#Imprimimos los datos de manera ordenada para verificar que el diccionario obtenido este correcto
for url, contenido in datos.items():
    print("URL:", url)
    print("Contenido:", contenido)
    print()