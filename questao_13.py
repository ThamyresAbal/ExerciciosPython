# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

arquivo = 'http://brasil.pyladies.com/about/'
html = csv = requests.get(arquivo, 'utf-8').text
soup = BeautifulSoup(html, 'html.parser')

palavras = {}
ladies = 0

for i in soup.body.find_all('p'):
	texto = i.text.strip()
	for j in texto.split(' '):
		palavras[j] = palavras.get(j, 0) + 1

print('a.')
print('Contagem == 1')
for i in palavras:
	if palavras[i] == 1:
		print(i)

print('\nb.')
print('Ladies:', palavras['ladies'])