# -*- coding: utf-8 -*-

import requests

generos = ['Action', 'Shooter', 'Platform', 'Skating']
arquivo = 'https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv'
ano_atual = 2019

# Colunas
__NAME__ = 0
__PLATFORM__ = 1
__YEAR_OF_RELEASE__ = 2
__GENRE__ = 3
__PUBLISHER__ = 4
__NA_SALES__ = 5
__EU_SALES__ = 6
__JP_SALES__ = 7
__OTHER_SALES__ = 8
__GLOBAL_SALES__ = 9
__CRITIC_SCORE__ = 10
__CRITIC_COUNT__ = 11
__USER_SCORE__ = 12
__USER_COUNT__ = 13
__DEVELOPER__ = 14
__RATING__ = 15

marcas = {}
csv = requests.get(arquivo).text.splitlines()  # Lista de linhas

for i in range(1, len(csv)):
    linha = csv[i].split(',')

    if linha[__GENRE__] in generos:
        m = linha[__PUBLISHER__]
        if m not in marcas:
            marcas[m] = {
                'publicacoes': 0,
                'globalsales': 0.0,
                'jppublicacoes': 0,
                'jpsales': 0
            }

        marcas[m]['publicacoes'] = marcas[m]['publicacoes'] + 1
        marcas[m]['globalsales'] = marcas[m]['globalsales'] + float(linha[__GLOBAL_SALES__])
        # print(m, marcas[m]['globalsales'])

        release = linha[__YEAR_OF_RELEASE__]
        if release != 'N/A' and release != '' and int(release) <= ano_atual - 10:
            if float(linha[__JP_SALES__]) > 0:
                marcas[m]['jppublicacoes'] = marcas[m]['jppublicacoes'] + 1
                marcas[m]['jpsales'] = marcas[m]['jpsales'] + float(linha[__JP_SALES__])

lista = []
for i in marcas:
    lista.append((marcas[i]['publicacoes'], i))

print('a.')
lista = sorted(lista, reverse=True)
for i in range(min(3, len(lista))):
    print('Marca:', lista[i][1].ljust(35), 'Publicacoes:', lista[i][0])

lista = []
for i in marcas:
    lista.append((marcas[i]['globalsales'], i))

print('b.')
lista = sorted(lista, reverse=True)
for i in range(min(3, len(lista))):
    print('Marca:', lista[i][1].ljust(35), 'Vendas:', lista[i][0])

lista = []
for i in marcas:
    lista.append((marcas[i]['jppublicacoes'], i))

print('c.')
lista = sorted(lista, reverse=True)
for i in range(min(3, len(lista))):
    print('Marca:', lista[i][1].ljust(35), 'Publicacoes Japao Ultimos 10 Anos:', lista[i][0])

lista = []
for i in marcas:
    lista.append((marcas[i]['jpsales'], i))

print('d.')
lista = sorted(lista, reverse=True)
for i in range(min(3, len(lista))):
    print('Marca:', lista[i][1].ljust(35), 'Vendas Japao Ultimos 10 Anos:', lista[i][0])