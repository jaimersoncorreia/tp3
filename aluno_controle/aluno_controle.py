from math import sin, cos, pi
from OpenGL.GL import *
from OpenGL.GLUT import *

# Aqui voce deve definir o corpo desta funcao de modo a incluir as
# transofmacoes, repeticoes, condicionais, etc. necessarias para concluir
# os exercicios.
#
# Pequena referencia rapida das funcoes mais usadas:
#
# - Translacao: glTranslate(dx, dy, dz)
#
# - Rotacao: glRotate(angle, axis_x, axis_y, axis_z)
#
# - Escala: glScale(sx, sy, sz)
#
# - Espelhamento: Usar escala com fator de -1.0 no eixo em relacao ao qual a
#   escala deve ocorrer.


import time

def compor_cena_cronometro(c):
    tempo = glutGet(GLUT_ELAPSED_TIME) / 1000
    angulo = tempo * 72

    # glRotate(tempo * 72, 0, 0, 1)

    # glRotate(tempo * 72, 0, 0, 1)  # 2a transformacao
    # glTranslate(1, 0, 0)           # 1a transformacao

    # glTranslate(1 * cos(angulo*pi/180),
    #             1 * sin(angulo*pi/180), 0)

    # escala = 0.2 * cos(360 * tempo *pi/180) + 1
    # glScale(escala, escala, escala)

    fracionario = (2*tempo) - int(2*tempo)

    y = -8 * fracionario**2 + 8 * fracionario - 1
    glTranslate(0, y, 0)
    glRotate(tempo * 72, 0, 0, 1)

    glBegin(GL_QUADS)
    glVertex(-0.5, -0.5, 0)
    glVertex(0.5, -0.5, 0)
    glVertex(0.5, 0.5, 0)
    glVertex(-0.5, 0.5, 0)
    glEnd()


tempo_anterior = 0.0
pos_x = 0.0
pos_y = 0.0
vel_x = 0.0
vel_y = 0.0


def compor_cena(c):
    global tempo_anterior, pos_x, pos_y

    tempo_agora = glutGet(GLUT_ELAPSED_TIME) / 1000
    dt = tempo_agora - tempo_anterior
    tempo_anterior = tempo_agora

    pos_x += vel_x * dt
    pos_y += vel_y * dt

    glTranslate(pos_x, pos_y, 0)

    glBegin(GL_QUADS)
    glVertex(-0.5, -0.5, 0)
    glVertex(0.5, -0.5, 0)
    glVertex(0.5, 0.5, 0)
    glVertex(-0.5, 0.5, 0)
    glEnd()


def processar_teclado(key):
    global vel_x, vel_y

    if key == b'a':
        vel_x -= 1
    elif key == b'd':
        vel_x += 1
    elif key == b'q':
        vel_y += 1
    elif key == b's':
        vel_y -= 1













