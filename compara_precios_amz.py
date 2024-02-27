from urllib.parse import urljoin
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.es/s?k=sartenes+antiadherentes&crid=932VOI9PKIP8&sprefix=%2Caps%2C98&ref=nb_sb_ss_recent_1_0_recent'
headers = {'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'es-ES,es;q=0.9',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0 (Edition std-1)'}


def info_producto(url):
    respuesta = requests.get(url, headers=headers)
    print(respuesta.status_code)
    if(respuesta.status_code != 200):
        print(respuesta)

    soup = BeautifulSoup(respuesta.text, 'lxml')
    titulo_scrap = soup.select_one('#productTitle')
    titulo = titulo_scrap.text.strip()
    precio_scrap = soup.select_one('span.a-offscreen')
    precio = precio_scrap.text
    valoracion_scrap = soup.select_one('#acrPopover')
    valoracion_text = valoracion_scrap.attrs.get('title')
    valoracion = valoracion_text.replace('de 5 estrellas', "")
    descripcion_scrap = soup.select_one('#feature-bullets')
    descripcion = descripcion_scrap.text.strip()

    return{

        "Titulo": titulo,
        "Precio": precio,
        "Valoracion": valoracion,
        "Descripcion": descripcion
    }

def info_productos_busqueda(url_busqueda):
    datos = []
    respuesta = requests.get(url_busqueda, headers=headers)
    print(respuesta.status_code)
    if(respuesta.status_code != 200):
        print(respuesta)

    soup = BeautifulSoup(respuesta.text, 'lxml')
    urls_productos = soup.select('[data-asin] h2 a')
    for url in urls_productos:
        url_completa = urljoin(url_busqueda, url.attrs.get('href'))
        info = info_producto(url_completa)
        datos.append(info)

    siguiente_pagina = soup.select_one('a:contains("Next")')
    if siguiente_pagina:
        siguiente_url = siguiente_pagina.attrs.get('href')
        siguiente_url = urljoin(url_busqueda, siguiente_url)
    
    df = pd.DataFrame(datos)
    df.to_json('info_amazon.json', orient='records', indent=4, force_ascii= False)

info_productos_busqueda(url)
