from pygame import *
import pygame
import os

WIDTH = 500
HEIGHT = 500
SCREEN = pygame.display.set_mode((HEIGHT,WIDTH))
PATH = os.path.dirname(__file__)
image_folder = os.path.join(PATH, 'data')
is_blit = False
black_color = (0,0,0)
class Arrow(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load(f'{image_folder}/arrow.png').convert()
        self.image.set_colorkey(Color('black'))
        self.rect = self.image.get_rect()
    def update(self, pos):
        self.rect.left = pos[0]
        self.rect.top = pos[1]

if __name__ == '__main__':
    pygame.init()
    bg = Surface((WIDTH,HEIGHT))
    ar = Arrow()
    bg.fill(black_color)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                pos = event.pos
                ar.update(pos)
        SCREEN.blit(bg, (0,0))
        if pygame.mouse.get_focused():
            pygame.mouse.set_visible(False)
            SCREEN.blit(ar.image, ar.rect)
        else:
            pygame.mouse.set_visible(True)
        pygame.display.flip()



