
import requests

arquivo = 'https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv'

paises = ['DEN', 'SWE', 'NOR']
esportes = ['Curling', 'Skating', 'Skiing', 'Ice Hockey']
medalha = 'Gold'
ouro = {'DEN': 0, 'SWE': 0, 'NOR': 0}
lista_contar_paises = {}

__ANO__ = 0
__CIDADE__ = 1
__ESPORTE__ = 3
__PAIS__ = 4
__GENERO__ = 6
__MEDALHA__ = 7

csv = requests.get(arquivo).text
for linha in csv.splitlines():
    linha = linha.split(',')

    # Primeira linha
    if linha[__ANO__] == 'Year':
        continue

    # a
    if int(linha[__ANO__]) >= 2001:
        if linha[__PAIS__] in paises:
            if linha[__ESPORTE__] in esportes:
                if linha[__MEDALHA__] == medalha:
                    ouro[linha[__PAIS__]] = ouro[linha[__PAIS__]] + 1

    # b
    if linha[__PAIS__] not in lista_contar_paises:
        lista_contar_paises[linha[__PAIS__]] = {
            'Nome': linha[__PAIS__],
            'Ano': [],
            'Cidade': [],
            'Esporte': [],
            'Genero': []
        }

    lista_contar_paises[linha[__PAIS__]]['Ano'].append(linha[__ANO__])
    lista_contar_paises[linha[__PAIS__]]['Cidade'].append(linha[__CIDADE__])
    lista_contar_paises[linha[__PAIS__]]['Esporte'].append(linha[__ESPORTE__])
    lista_contar_paises[linha[__PAIS__]]['Genero'].append(linha[__GENERO__])

# a
max_val = -1
max_pais = ''

for pais, valor in ouro.items():
    if valor > max_val:
        max_val = valor
        max_pais = pais

print('O pais com mais medalhas de ouro:', max_pais)

print('\nRELATORIO')
for pais, dados in lista_contar_paises.items():
    print('PAIS:', pais)
    print('MEDALHAS:', len(dados['Ano']))
    print('ANO'.ljust(10), 'CIDADE'.ljust(20), 'ESPORTE'.ljust(15), 'GENERO')

    for i in range(len(dados['Ano'])):
        print(dados['Ano'][i].ljust(10),
              dados['Cidade'][i].ljust(20),
              dados['Esporte'][i].ljust(15),
              dados['Genero'][i])

    print("")