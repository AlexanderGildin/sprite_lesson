import pygame
import os
from random import randint

WIDTH = 500
HEIGHT = 500
SCREEN = pygame.display.set_mode((HEIGHT, WIDTH))
PATH = os.path.dirname(__file__)
image_folder = os.path.join(PATH, 'data')
is_blit = False
black_color = (0, 0, 0)


class Bomb(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.is_boom = False
        self.image = pygame.image.load(f'{image_folder}/bomb.png')
        self.rect = self.image.get_rect()
        self.rect.left = pos[0]
        self.rect.top = pos[1]

    def update(self, pos):
        if not self.is_boom:
            if pos[0] >= self.rect.left and pos[0] <= self.rect.right:
                if pos[1] >= self.rect.top and pos[1] <= self.rect.bottom:
                    self.image = pygame.image.load(f'{image_folder}/boom.png')
                    self.is_boom = True
                    self.rect.top = self.rect.top - 30
                    self.rect.left = self.rect.left - 30


entity = pygame.sprite.Group()
for _ in range(15):
    bomb = Bomb([randint(70, 400), randint(70, 400)])
    entity.add(bomb)

if __name__ == '__main__':
    pygame.init()
    bg = pygame.Surface((WIDTH, HEIGHT))
    tick = pygame.time.Clock()
    bg.fill(black_color)
    posit = 0, 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                posit = event.pos
        tick.tick(30)
        SCREEN.blit(bg, (0, 0))
        entity.update(posit)
        for i in entity:
            SCREEN.blit(i.image, i.rect)
        pygame.display.flip()
