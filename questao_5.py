#usar o turtle para desenhar a imagem

import turtle

def quadrado(x, y, l):
    #cores
    turtle.pencolor('black')
    turtle.fillcolor('white')

    #rotina
    # Linha que manda levantar a caneta
    turtle.penup()

    #start
    turtle.goto((x, y))  # Inicio
    turtle.pendown()  #abaixa a caneta
    turtle.goto((x, y + l))  #para cima
    turtle.goto((x + l, y + l))  #para direita
    turtle.goto((x + l, y))  #para baixo
    turtle.goto((x, y))  #para esquerda

    #fim da rotina
    turtle.end_fill()
    turtle.penup()

def circulo(x, y, d):
    turtle.pencolor('black')
    turtle.fillcolor('white')

    turtle.penup()  # Levanta caneta
    turtle.goto((x, y))  # Inicio
    turtle.pendown()  # Baixa caneta
    turtle.circle(d)

    turtle.end_fill()
    turtle.penup()


def desenha(x, y, l, c):
    if c == 0:
        return

    print(x, y, l, c)
    x_circulo = x + (l * 0.75)
    x_quadrado = x + (l * 0.05)

    quadrado(x, y, l)
    circulo(x_circulo, y + int(l * 0.05), int(l * 0.22))
    circulo(x_circulo, y + int(l * 0.51), int(l * 0.22))
    quadrado(x_quadrado, y + int(l * 0.51), int(l * 0.44))
    quadrado(x_quadrado, y + int(l * 0.05), int(l * 0.44))

    desenha(x_quadrado, y + int(l * 0.05), int(l * 0.44), c - 1)


#primeiro quadrado a ser desenhado
x = -200
y = -200
l = 400

#finalizando o processo
desenha(x,y,l,5)
turtle.done()