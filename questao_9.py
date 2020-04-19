# Bibliotecas
import time
import subprocess
#import questao8a
#import questao8b
#import questao8c

def print_tempo(diferenca):
	print('> Tempo %dm:%ds' % (diferenca // 60, diferenca % 60))
# Main
def main():

    print("Programa letra A")
    args_a = "python questao8a.py " 
    inicio = time.time()
    #questao8a.inicia8a()
    subprocess.call(args_a) 
    agora_A = (time.time() - inicio) * 1000
    

    print("Programa letra B")
    args_b = "python questao8b.py"
    inicio = time.time()
    #questao8b.inicia8b()
    subprocess.call(args_b)
    agora_B = (time.time() - inicio) * 1000

    print("Programa letra C")
    args_c = "python questao8c.py"
    inicio = time.time()
    #questao8c.inicia8c()
    subprocess.call(args_c)
    agora_C = (time.time() - inicio) * 1000 
    
    #Tempos dos programas
    print("Tempo do programa A")
    print_tempo(agora_A)
    print("Tempo do programa B")
    print_tempo(agora_B)
    print("Tempo do programa C")
    print_tempo(agora_C)


# Rodando o main
if __name__ == '__main__':
    main()
    
