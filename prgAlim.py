import pygame
import os

WIDTH = 500
HEIGHT = 500
SCREEN = pygame.display.set_mode((HEIGHT,WIDTH))
PATH = os.path.dirname(__file__)
image_folder = os.path.join(PATH, 'data')
is_blit = False
black_color = (0,0,0)
speed = 10
class Char(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f'{image_folder}/hero.png').convert()
        self.image.set_colorkey(pygame.Color('white'))
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 0
    def update(self):
        self.rect.top += speed_y
        self.rect.left+=speed_x


if __name__ == '__main__':
    pygame.init()
    bg = pygame.Surface((WIDTH,HEIGHT))
    hero = Char()
    tick = pygame.time.Clock()
    bg.fill(black_color)
    speed_x = 0
    speed_y = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    speed_y -=10
                if event.key == pygame.K_DOWN:
                    speed_y+=10
                if event.key == pygame.K_LEFT:
                    speed_x -= 10
                if event.key == pygame.K_RIGHT:
                    speed_x+=10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    speed_y +=10
                if event.key == pygame.K_DOWN:
                    speed_y-=10
                if event.key == pygame.K_LEFT:
                    speed_x += 10
                if event.key == pygame.K_RIGHT:
                    speed_x-=10
        tick.tick(30)
        SCREEN.blit(bg, (0,0))
        hero.update()
        SCREEN.blit(hero.image, hero.rect)
        pygame.display.flip()



