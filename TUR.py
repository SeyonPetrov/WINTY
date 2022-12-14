import pygame as pg
import os

pg.init()
screen = pg.display.set_mode((300, 300))
pg.display.set_caption("Свой курсор мыши")

im = pg.image.load(os.path.join('data', 'creature.png'))  # загружаем изображение персонажа
scrn = pg.Surface((83, 101))
scrn.blit(im, (0, 0))  # располагаем его на отдельном холсте

clock = pg.time.Clock()
go = True
x = y = 0
while go:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            go = False
        if pg.key.get_pressed()[pg.K_UP]:  # при нажатии на стрелку "вверх"
            y -= 10  # двигаем в отрицательную сторону по оси ординат
        if pg.key.get_pressed()[pg.K_DOWN]:  # при нажатии на стрелку "вниз"
            y += 10  # перемещаем в положительную сторону по оси ординат
        if pg.key.get_pressed()[pg.K_RIGHT]:  # при нажатии на стрелку "вправо"
            x += 10  # двигаемся в положительную сторону оси абцисс
        if pg.key.get_pressed()[pg.K_LEFT]:  # при нажатии на стрелку "влево"
            x -= 10  # перемещаемся в отрицательную сторону по оси абцисс

    screen.fill(('white'))  # красим фон в белый
    screen.blit(scrn, (x, y))  # рисуем нашего персонажа на основном холсте
    pg.display.flip()
    clock.tick(60)

pg.quit()
