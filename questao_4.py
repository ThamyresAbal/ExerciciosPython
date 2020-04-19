#lendo ventor de 5 número int e printando invertido

lista = []
for i in range(5):
    valor = int(input('Digite um valor para o índice '+ str(i) + ':'))
    lista.insert(0, valor)
print(lista)
