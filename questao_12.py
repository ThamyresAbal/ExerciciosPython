# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

arquivo = 'https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html'
html = csv = requests.get(arquivo).text
estados_centro = ['GO', 'MT', 'MS', 'DF']

soup = BeautifulSoup(html, 'html.parser')
print('a.')
print(soup.body.div.article.center.div.contents)

print('b.')
estado = input('Digite a UF do estado: ')

if estado in estados_centro:
	sair = False
	for i in soup.body.div.article.center.div.find_all('div'):
		if 'celula' in i.get('class'):
			if i.text == estado:
				sair = True

			if sair:
				print(i.text, end=' ')
		elif sair:
			break
else:
	print('Estado não está na lista')
