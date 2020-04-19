n = input('Digite o valor de n: ')
n = int(n) # N deve ser um inteiro

acumulador = 0

for i in range(2,n+1,2): # Pulando de 2 em 2
	acumulador = acumulador + i

print ('Resultado da soma: ', acumulador)