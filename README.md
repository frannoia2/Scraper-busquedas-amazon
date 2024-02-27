# Scraper-busquedas-amazon 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

**Script para scrapear la información de los productos de una búsqueda en Amazon.**

## Funcionamiento:
Este script utiliza la url de la búsqueda que deseemos en Amazon para obtener la info de cada uno de los productos y devolverla en formato JSON con la siguiente estructura:

```
    {
        "Titulo": titulo,
        "Precio": precio,
        "Valoracion": valoracion,
        "Descripcion": descripcion
    }    
    
```