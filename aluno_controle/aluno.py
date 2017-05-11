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
def compor_cena(c):
	tempo = glutGet(GLUT_ELAPSED_TIME)/1000
	
	print(tempo)
	
	glRotate(tempo * 72,0,0,1)
	glBegin(GL_QUADS)
	glVertex(-0.5, -0.5, 0)
	glVertex(0.5, -0.5, 0)
	glVertex(0.5, 0.5, 0)
	glVertex(-0.5, 0.5, 0)
	
	glEnd()
	time.sleep(0.1)
