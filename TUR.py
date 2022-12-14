import pygame as pg
import os

pg.init()
screen = pg.display.set_mode((600, 400))
pg.display.set_caption("Свой курсор мыши")

im = pg.image.load(os.path.join('data', 'arrow.png'))  # загружаем изображение
scrn = pg.Surface((50, 50))
scrn.blit(im, (0, 0))  # располагаем его на отдельном холсте
cur = pg.cursors.Cursor((0, 0), scrn)  # создаем курсор из нашего холста
pg.mouse.set_cursor(cur)  # устанавливаем созданный курсор

clock = pg.time.Clock()
go = True
while go:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            go = False

    screen.fill((0, 0, 0))
    pg.display.flip()
    clock.tick(60)

pg.quit()
