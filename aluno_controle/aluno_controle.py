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


tempo_anterior = 0.0
pos_x = 0.0
pos_y = 0.0
pos_t = 0.0
vel_x = 0.0
vel_y = 0.0
vel_t = 0.0








def compor_cena(c):
    global tempo_anterior, pos_x, pos_y, pos_t

    tempo_agora = glutGet(GLUT_ELAPSED_TIME) / 1000
    dt = tempo_agora - tempo_anterior
    tempo_anterior = tempo_agora

    pos_x += vel_x * dt
    pos_y += vel_y * dt
    pos_t += vel_t * dt

    glTranslate(pos_x, pos_y, 0)
    glRotate(pos_t * 15, 0, 0, 1)

    glBegin(GL_QUADS)
    glVertex(-0.5, -0.5, 0)
    glVertex(0.5, -0.5, 0)
    glVertex(0.5, 0.5, 0)
    glVertex(-0.5, 0.5, 0)
    glEnd()


def processar_teclado(key):
    global vel_x, vel_y, vel_t

    if key == b'a':
        vel_x -= 1
    elif key == b'd':
        vel_x += 1
    elif key == b'q':
        vel_y += 1
    elif key == b's':
        vel_y -= 1
    elif key == b'z':
        vel_t -= 1
    elif key == b'c':
        vel_t += 1
    elif key == b' ':
        vel_t = vel_x = vel_y = 0












