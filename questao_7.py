import random
import pygame
from pygame.locals import *

#tela e cores
(width, height) = (500, 500)
branco = (255, 255, 255)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
amarelo = (255, 255, 0)
pygame.init()
tela = pygame.display.set_mode((width, height))

#fundo
tela.fill(branco)

ret = pygame.rect.Rect((round(width/2)-25, round(height/2)-25, 50, 50))

clock = pygame.time.Clock()

Terminou = False
while not Terminou:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Terminou = True

        #barra de espaços
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ret = pygame.rect.Rect((random.randrange(0, 500), random.randrange(0, 500), 50, 50))
                pygame.draw.rect(tela, amarelo, ret)

        #mouse direito
        if event.type == MOUSEBUTTONDOWN and event.button == 3:
            ret = pygame.rect.Rect((random.randrange(0, 500), random.randrange(0, 500), 50, 50))
            pygame.draw.rect(tela, amarelo, ret)

    pygame.draw.rect(tela, amarelo, ret)
    pygame.display.update()

    clock.tick(40)
    pygame.display.update()
pygame.quit()
