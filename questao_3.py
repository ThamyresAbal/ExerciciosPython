def potencia(a,b):
    acumulador = 1
    for i in range(b):
        acumulador = acumulador * a
    return acumulador

#obtendo e imprimindo o resultado
a = int(input('Diqite um valor para A: '))
b = int(input('Digite um valor para B: '))
print('Resultado: ', potencia(a,b))