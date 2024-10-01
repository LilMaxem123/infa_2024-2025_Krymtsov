import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((600, 400))

# Здесь мы будем рисовать

# создадим функцию рисования слоев неба
def DrawSky(col1, col2, col3, x1, y1, x2, y2):
    rect(screen, (col1, col2, col3), (x1, y1, x2, y2))

# нарисуем слои неба
    
DrawSky(250, 214, 165, 0, 0, 600, 75)
DrawSky(222, 184, 135, 0, 75, 600, 75)
DrawSky(244, 164, 96, 0, 150, 600, 75)
DrawSky(188, 143, 143, 0, 225, 600, 175)

# создадим функцию рисования вершин гор
def DrawMountain(col1, col2, col3, x1, y1, x2, y2, x3, y3):
    # Создаем список координат вершин
    vertices = [(x1, y1), (x2, y2), (x3, y3)]  
    polygon(screen, (col1, col2, col3), vertices)

# нарисуем верхний ряд гор
    
DrawMountain(244, 164, 96, 0, 150, 100, 150, 50, 20)
DrawMountain(244, 164, 96, 200, 150, 300, 150, 250, 20)
DrawMountain(244, 164, 96, 400, 150, 500, 150, 450, 20)


# нарисуем нижний ряд гор
DrawMountain(188, 143, 143, 20, 300, 260, 300, 150, 20)
DrawMountain(188, 143, 143, 300, 300, 400, 300, 350, 20)
DrawMountain(188, 143, 143, 500, 300, 600, 300, 550, 20)

# нарисуем солнце

circle(screen, (218, 165, 32), (300, 75), 100)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
