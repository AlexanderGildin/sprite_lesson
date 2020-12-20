import os
import sys
import pygame
import random

pygame.init()
size = width, height = 470, 800
screen = pygame.display.set_mode(size)


class My_toy(pygame.sprite.Sprite):
    def __init__(self, pic, x_pos):
        super().__init__()
        self.image = load_image(pic)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = random.randint(10, 710)
        self.y = self.rect.y
        self.delta_y = (random.randint(6, 20)) / 10
        if self.rect.y % 2 == 0:
            self.delta_y *= -1
        print(self.delta_y)

    def update(self, *args, **kwargs):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN \
                and self.rect.collidepoint(args[0].pos):
            self.delta_y *= -1
        # self.rect.move(0, self.delta_y)
        self.y += self.delta_y
        if self.y < 10:
            self.y = 10
            self.delta_y = (random.randint(6, 20)) / 10
        if self.y > 710:
            self.y = 710
            self.delta_y = -(random.randint(6, 20)) / 10
        self.rect.y = self.y

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


bkground_sprite = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
for i in range(10, 400, 62):
    # sprite = pygame.sprite.Sprite()
    # sprite.image = load_image(random.choice(["picg1.png", "picg2.png", "picg3.png"]))
    # sprite.rect = sprite.image.get_rect()
    # sprite.rect.x = i
    # sprite.rect.y = random.randint(10, 710)
    sprite = My_toy(random.choice(["picg1.png", "picg2.png", "picg3.png"]), i)
    all_sprites.add(sprite)

fon = load_image("img1v.jpg")
doing = True
fps = 30
tick = pygame.time.Clock()
while doing:
    # screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.update(event)
            for k in all_sprites:
                print(k.rect.y, k.delta_y)
            print()
    tick.tick(fps)

    screen.blit(fon, (0, 0))  # вывод сурфейса на экран
    all_sprites.draw(screen)  # вывод комплекта спрайтов на экран
    for toy in all_sprites:
        x = toy.rect.x + toy.rect.width / 2
        y = toy.rect.y
        pygame.draw.line(screen, (0, 0, 180), (x, 0), (x, y))
    pygame.display.flip()
    all_sprites.update()
pygame.quit()

