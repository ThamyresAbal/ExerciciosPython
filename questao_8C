import multiprocessing
from multiprocessing import Queue

vetorA = [1, 2, 3, 4, 5, 6, 11, 12, 23, 15, 5, 34, 54, 65, 6, 23, 43]
N = len(vetorA)
vetorB = []
queue = Queue()


def fatorialthreads(vetorA, inicio, fim, queue):
    vetor = []
    for i in range(inicio, fim):
        vetor.append(fatorial(vetorA[i]))
    queue.put(vetor)

def fatorial(n):
  fat = n
  for i in range(n - 1, 1, -1):
    fat = fat * i
  return fat


p0 = multiprocessing.Process(target=fatorialthreads, args=(vetorA, 0, N/4, queue))
p0.start() # inicia processo 0


p1 = multiprocessing.Process(target=fatorialthreads, args=(vetorA, int(N/4), int(N/2), queue))
p1.start() # inicia processo 1


p2 = multiprocessing.Process(target=fatorialthreads, args=(vetorA, int(N/2), int((3 * N)/4), queue))
p2.start() # inicia processo 2


p3 = multiprocessing.Process(target=fatorialthreads, args=(vetorA, int((3 * N)/4), N, queue))
p3.start() # inicia processo 3

p0.join() # espera processo 0
p1.join() # espera processo 1
p2.join() # espera processo 0
p3.join() # espera processo 1

while not queue.empty():
    vetorB + queue.get()

print(vetorB)
