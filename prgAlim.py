import pygame
from pygame import *
import os

self_path = os.path.dirname(__file__)
images = os.path.join(self_path, 'data')
BLOCK_SIZE = 50
WIDTH = 550
HEIGHT = 550
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
LEVEL = [
    '...###.....',
    '..##.#.####',
    '.##..###..#',
    '##........#',
    '#...@..#..#',
    '###..###..#',
    '..#..#....#',
    '.##.##.#.##',
    '.#......##.',
    '.#.....##..',
    '.#######...',
]


class Void(sprite.Sprite):
    def __init__(self, row, col):
        sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f'{images}/grass.png')
        self.rect = Rect(row, col, BLOCK_SIZE, BLOCK_SIZE)


class Border(sprite.Sprite):
    def __init__(self, row, col):
        sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f'{images}/box.png')
        self.rect = Rect(row, col, BLOCK_SIZE, BLOCK_SIZE)


class Character(sprite.Sprite):
    def __init__(self, row, col):
        sprite.Sprite.__init__(self)
        self.bg = Void(row, col)
        self.image = pygame.image.load(f'{images}/mar.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = row + 13, col + 5

    def update(self):
        global left, right, down, up
        if left:
            cah.rect.x -= BLOCK_SIZE
            self.collision()
            left = False
        elif right:
            cah.rect.x += BLOCK_SIZE
            self.collision()
            right = False
        elif up:
            cah.rect.y -= BLOCK_SIZE
            self.collision()
            up = False
        elif down:
            cah.rect.y += BLOCK_SIZE
            self.collision()
            down = False

    def collision(self):
        for a in entity:
            if sprite.collide_rect(self, a):
                if type(a) == Border:
                    if left:
                        cah.rect.x += BLOCK_SIZE
                    elif right:
                        cah.rect.x -= BLOCK_SIZE
                    elif up:
                        cah.rect.y += BLOCK_SIZE
                    elif down:
                        cah.rect.y -= BLOCK_SIZE


entity = sprite.Group()
x, y = 0, 0
for i in LEVEL:
    for j in i:
        if j == '.':
            k = Void(x, y)
            entity.add(k)
        elif j == '#':
            k = Border(x, y)
            entity.add(k)
        elif j == '@':
            x_char, y_char = x, y
        x += BLOCK_SIZE
    y += BLOCK_SIZE
    x = 0
cah = Character(x_char, y_char)
entity.add(cah)
if __name__ == '__main__':
    pygame.init()
    left, right, up, down = False, False, False, False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    up = True
                elif event.key == pygame.K_DOWN:
                    down = True
                elif event.key == pygame.K_RIGHT:
                    right = True
                elif event.key == pygame.K_LEFT:
                    left = True
        cah.update()
        for k in entity:
            if type(k) == Character:
                SCREEN.blit(k.bg.image, k.bg.rect)
                SCREEN.blit(k.image, k.rect)
            SCREEN.blit(k.image, k.rect)
        pygame.display.flip()
