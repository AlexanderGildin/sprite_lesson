import os
import sys

import pygame

def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

all_sprites = pygame.sprite.Group()

sprite = pygame.sprite.Sprite()
sprite.image = load_image("arrow.png")
sprite.rect = sprite.image.get_rect()
all_sprites.add(sprite)
if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
ok = False
while running:
    screen.fill('BLACK')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            sprite.rect.x = event.pos[0]
            sprite.rect.y = event.pos[1]
            image = load_image("arrow.png")
            ok = True
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
                ok = True
            else:
                ok = False
    if ok:
        screen.blit(image, (sprite.rect.x, sprite.rect.y))
    pygame.display.flip()
    clock.tick(144)
