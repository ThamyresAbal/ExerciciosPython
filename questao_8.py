import random
import pygame
from pygame.locals import *

(width, height) = (500, 500)
branco = (255, 255, 255)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
amarelo = (255, 255, 0)
pygame.init()
pygame.font.init()
tela = pygame.display.set_mode((width, height))
multiplicador_velocidade = 0
lista_quadrados = []

center = [250,250]
radius = 30

ret = pygame.Rect(center[0]-radius, center[1]-radius, \
                    radius*2, radius*2)

clock = pygame.time.Clock()

Terminou = True
while (Terminou == True):

   tela.fill(branco)
   config_fonte = pygame.font.SysFont('Times', 20)
   textsurface = config_fonte.render('Clique aqui!', False, (0, 0, 0))
   tela.blit(textsurface, (200, 200))

   for i in lista_quadrados:
       pygame.draw.rect(tela, vermelho, i, 0)

   pygame.display.flip()
   pygame.draw.circle(tela, azul, ret.center, radius)
   pygame.display.update()

   clock.tick(30)

   for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             Terminou = False
             break
        if event.type == MOUSEBUTTONDOWN:
            x = (event.pos[0])
            y = (event.pos[1])
            print(ret.collidepoint(x,y))
            if ret.collidepoint(x,y) == 1:
                retnovo = pygame.rect.Rect((random.randrange(0, 500), random.randrange(0, 500) , 50, 50))

                lista_quadrados.append(retnovo)
                for i in lista_quadrados:
                    print(i)
                    for j in lista_quadrados:
                        if i == j:
                            continue
                        if i.colliderect(j):
                            lista_quadrados.remove(i)
                            lista_quadrados.remove(j)

            pygame.draw.circle(tela, azul, ret.center, radius)
clock.tick(40)
   pygame.display.update()
pygame.quit()
