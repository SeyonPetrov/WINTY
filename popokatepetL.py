import pygame


size = width, height = 501, 501
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
v = 0.75
run = True
go = False
x, y = 251, 251
x_new, y_new = 251, 251
color = pygame.Color('red')
while run:
    screen.fill(('black'))
    pygame.draw.circle(screen, color, (int(x), int(y)), 20)  # рисуем наш круг
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

        if e.type == pygame.MOUSEBUTTONUP and e.button == 1:  # обрабатываем событие мыши и получаем координаты
            x_new, y_new = pygame.mouse.get_pos()

    if x > x_new:  # запускаем сравние координат центра круга и расположения курсора
        x -= v
    elif x < x_new:
        x += v
    if y > y_new:
        y -= v
    elif y < y_new:
        y += v

    pygame.display.flip()
    clock.tick(170)  # устанавливаем задержку в 170 кадров в секунду
pygame.quit()
