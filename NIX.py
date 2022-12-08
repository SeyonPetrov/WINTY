import pygame


if __name__ == '__main__':
    pygame.init()
    size = width, height = 700, 400
    screen = pygame.display.set_mode(size)
    for_cir = []
    running = True
    GO = False
    pos = (0, 0)
    clock = pygame.time.Clock()
    speed_x = 300 * clock.tick() // 1000 * -1
    speed_y = 300 * clock.tick() // 1000 * -1
    while running:
        for event in pygame.event.get():
            scrn = pygame.Surface(screen.get_size())
            if event.type == pygame.QUIT:
                running = False
            if pygame.mouse.get_pressed() == (1, 0, 0):
                GO = True
                pos = pygame.mouse.get_pos()
                for_cir.append(pos)
        print(pos)
        if GO:

            for r in range(len(for_cir)):
                x = for_cir[r][0]
                y = for_cir[r][1]

                if (x - 10) - speed_x <= 0:
                    speed_x = speed_x * -1
                elif (x - 10) + speed_x >= width:
                    speed_x = speed_x * -1
                elif (y - 10) - speed_y <= 0:
                    speed_y = speed_y * -1
                elif (y - 10) >= height:
                    speed_y = speed_y * -1
                else:
                    x += speed_x
                    y += speed_y
                    scrn.fill((0, 0, 0))
                pygame.draw.circle(scrn, ('white'), (x, y), 10)

            screen.blit(scrn, (0, 0))
        pygame.display.flip()
    pygame.quit()