import os
import sys
import pygame

# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
size = width, height = 600, 95
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


class Car(pygame.sprite.Sprite):
    image = load_image("car.png")

    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.image = Car.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.n = 0
        self.flag = 0
        self.p = 0

    def update(self):
        if self.rect.x == 450:
            self.flag = 1
            self.image = pygame.transform.flip(self.image, True, False)
        elif self.rect.x == 0:
            self.flag = 0
            if self.p:
                self.image = pygame.transform.flip(self.image, True, False)

        if self.flag:
            self.rect.x -= 1
        else:
            self.rect.x += 1

        if not self.p:
            self.p += 1


Car(all_sprites)
clock = pygame.time.Clock()
run = True
while run:
    scrn = pygame.Surface(screen.get_size())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill('white')
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(230)
pygame.quit()
