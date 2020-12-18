import os
import sys

import pygame

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

all_sprites = pygame.sprite.Group()

sprite = pygame.sprite.Sprite()
sprite.image = load_image("car2.png")
sprite.rect = sprite.image.get_rect()
all_sprites.add(sprite)
if __name__ == '__main__':
    pygame.init()
    size = width, height = 600, 95
    screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
ok = False
image = load_image('car2.png')
dif_x = 1
while running:
    screen.fill('WHITE')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if sprite.rect.x == 460:
        dif_x *= -1
        image = pygame.transform.flip(image, True, False)
        if ok == False:
            ok = True
        else:
            ok = False
    if sprite.rect.x == 0:
        if ok:
            dif_x *= -1
            image = pygame.transform.flip(image, True, False)
            ok = False
    sprite.rect.x += dif_x
    screen.blit(image, (sprite.rect.x, sprite.rect.y))
    pygame.display.flip()
    clock.tick(144)