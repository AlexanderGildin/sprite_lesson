import pygame
import os

WIDTH = 500
HEIGHT = 500
SCREEN = pygame.display.set_mode((HEIGHT, WIDTH))
PATH = os.path.dirname(__file__)
image_folder = os.path.join(PATH, 'data')
is_blit = False
black_color = (0, 0, 0)


class Char(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = pygame.image.load(f'{image_folder}/car.png').convert()
        self.image.set_colorkey(pygame.Color('white'))
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 0

    def update(self):
        self.rect.left += self.speed
        if self.rect.right > 500:
            self.image = pygame.transform.flip(self.image, True, False)
            self.speed = -self.speed
        if self.rect.left < 0:
            self.image = pygame.transform.flip(self.image, True, False)
            self.speed = -self.speed


if __name__ == '__main__':
    pygame.init()
    bg = pygame.Surface((WIDTH, HEIGHT))
    hero = Char()
    tick = pygame.time.Clock()
    bg.fill(black_color)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        tick.tick(30)
        SCREEN.blit(bg, (0, 0))
        hero.update()
        SCREEN.blit(hero.image, hero.rect)
        pygame.display.flip()
