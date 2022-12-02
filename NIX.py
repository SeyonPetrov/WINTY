import pygame

WH = pygame.Color('white')
BK = pygame.Color('black')
a, n = 0, 0
try:  #
    a, n = list(map(lambda x: int(x), input().split()))
except ValueError:
    print('Неправильный формат ввода')


def draw_chess(screen):
    s = screen
    color = ''
    t = a // n  #

    if n % 2 == 0:  #
        color = WH
    else:
        color = BK

    for i in range(n):  #
        for j in range(n):
            print(color)
            rect = (i * t, j * t, t, t)
            pygame.draw.rect(s, color, rect)
            if color != WH:
                color = WH
            else:
                color = BK
        if n % 2 == 0:
            if color == WH:
                color = BK
            else:
                color = WH


if __name__ == '__main__':
    pygame.init()
    size = width, height = a, a
    screen = pygame.display.set_mode(size)
    draw_chess(screen)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()