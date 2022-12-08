import pygame

size = width, height = 600, 700
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('Шарики')
ran = True
rad = 10
color = pygame.Color('white')
circles = []
screen2 = pygame.Surface(screen.get_size())
while ran:
    for e in pygame.event.get():
        screen2 = pygame.Surface(screen.get_size())
        if e.type == pygame.QUIT:
            ran = False
        if e.type == pygame.MOUSEBUTTONUP:
            inf = list(e.pos) + [-1, -1]
            circles.append(inf)

    screen2.fill(0, 0, 0)
    for i in range(len(circles)):
        for cord in (0, 1):
            if circles[i][cord] >= width - 10 or circles[i][cord]:
                pass