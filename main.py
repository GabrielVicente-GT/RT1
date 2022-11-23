
#Gabriel Alejandro Vicente Lorenzo 20498
#RT1

from ray import *


r = Raytracer(800,600)
r.objetos = [
    #sONRISA
    Esfera(V3(0.8, -3.8, -16), 0.20),
    Esfera(V3(-0.8, -3.8, -16), 0.20),
    Esfera(V3(-0.3, -3.5, -16), 0.20),
    Esfera(V3(0.3, -3.5, -16), 0.20),

    #BOTONES
    Esfera(V3(0, -0.65, -16), 0.5),
    Esfera(V3(0, 1.3, -16), 0.55),
    Esfera(V3(0, 4.2, -16), 0.7),
    #NARIZ
    Esfera(V3(0, -4.5, -16), 0.5),
    #OJOS
    Esfera(V3(0.65, -5.5, -16), 0.15),
    Esfera(V3(0.7, -5.3, -16), 0.3),
    Esfera(V3(0.7, -5.3, -16), 0.35),
    Esfera(V3(-0.80, -5.7, -16), 0.15),
    Esfera(V3(-0.75, -5.5, -16), 0.3),
    Esfera(V3(-0.75, -5.5, -16), 0.35),
    #CUERPO
    Esfera(V3(0, 4.5, -16), 3),
    Esfera(V3(0, 4.5, -16), 3.1),
    Esfera(V3(0, -4.5, -16), 2),
    Esfera(V3(0, -4.5, -16), 2.1),
    Esfera(V3(0, -0.5, -16), 2.5),
    Esfera(V3(0, -0.5, -16), 2.6)]
r.colores = [
    #SONRISA
    color(0,0,0),
    color(0,0,0),
    color(0,0,0),
    color(0,0,0),

    #BOTONES
    color(0,0,0),
    color(0,0,0),
    color(0,0,0),

    #NARIZ
    color(243, 156, 18 ),
    #OJOS
    color(0,0,0),
    color(255,255,255),
    color(0,0,0),
    color(0,0,0),
    color(255,255,255),
    color(0,0,0),
    #CUERPO
    color(255,255,255),
    color(0,0,0),
    color(255,255,255),
    color(0,0,0),
    color(255,255,255),
    color(0,0,0)]

r.render()
r.write('rt1.bmp')
