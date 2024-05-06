# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:59:55 2024

@author: Dell
"""

" se muestra sin tildes ni ñ"

noticia = open("noticia.txt","rt")
datos_noticia = noticia.read()
print(datos_noticia)


"se muestra con tildes y ñ"

noticia = open("noticia.txt","rt",encoding='utf8')
datos_noticia = noticia.read()
print(datos_noticia)
