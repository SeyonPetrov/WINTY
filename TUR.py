import os
import sys
import pygame

# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
size = width, height = 600, 300
screen = pygame.display.set_mode(size)


def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname).convert_alpha()
    return image


all_sprites = pygame.sprite.Group()


class GameOver(pygame.sprite.Sprite):
    image = load_image("gameover.png")

    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.image = GameOver.image
        self.rect = self.image.get_rect()
        self.rect.x = -600
        self.rect.y = 0

    def update(self):
        if self.rect.x != 0:
            self.rect.x += 1


GameOver(all_sprites)
clock = pygame.time.Clock()
run = True
while run:
    scrn = pygame.Surface(screen.get_size())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill('blue')
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(200)
pygame.quit()
