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
sprite.image = load_image("creature.png")
sprite.rect = sprite.image.get_rect()
all_sprites.add(sprite)
if __name__ == '__main__':
    pygame.init()
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
ok = True
image = load_image('creature.png')
while running:
    screen.fill('WHITE')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                sprite.rect.x -= 10
            elif event.key == pygame.K_RIGHT:
                sprite.rect.x += 10
            elif event.key == pygame.K_DOWN:
                sprite.rect.y += 10
            elif event.key == pygame.K_UP:
                sprite.rect.y -= 10
    screen.blit(image, (sprite.rect.x, sprite.rect.y))
    pygame.display.flip()
    clock.tick(144)
