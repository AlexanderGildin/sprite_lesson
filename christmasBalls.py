import os
import sys
import pygame
import random
import time

pygame.init()
size = width, height = 480, 800
screen = pygame.display.set_mode(size)
state_mode = 0  # 0 - перед началом игры, 1 - уже щелкали мышкой, 2 - музыка
co = [(0, 0)] * 7  # массив координат шариков для проверки на выстроенность в линию
start_time_music = time.time()
number_music = 5
music_volume = 0.5
debug = False

class Math_line:
    delta_exp = 30  # допустимая погршешность при выстраивании линии

    @staticmethod
    def get_line(xl, yl, xr, yr):
        a = yl - yr
        b = xr - xl
        c = -(a * xl + b * yl)
        return (a, b, c)

    @staticmethod
    def one_line(xl, yl, xr, yr, xn, yn):
        a, b, c = Math_line.get_line(xl, yl, xr, yr)
        yp = (-c - a * xn) / b
        return abs(yn - yp) <= Math_line.delta_exp


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
        if debug:
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

if not os.path.isfile('data/d0.mp3'):
    print("Файл d0.mp3 не найден")
    sys.exit()
if not os.path.isfile('data/d1.mp3'):
    print("Файл d1.mp3 не найден")
    sys.exit()
if not os.path.isfile('data/d2.mp3'):
    print("Файл d2.mp3 не найден")
    sys.exit()
if not os.path.isfile('data/d3.mp3'):
    print("Файл d3.mp3 не найден")
    sys.exit()
if not os.path.isfile('data/d4.mp3'):
    print("Файл d4.mp3 не найден")
    sys.exit()
vin = load_image("vin.png")
startfon = load_image("startfon.jpg")
fon = load_image("img1v.jpg")
decor = load_image("img1vdecor.png")
begining = True
doing = True
screen.blit(startfon, (0, 0))
pygame.display.flip()

while begining:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doing = False
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == 27:
            doing = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            begining = False

fps = 30
tick = pygame.time.Clock()
while doing:
    # screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if debug:
            print(event)
        if event.type == pygame.KEYDOWN and event.key == 27:
            doing = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            music_volume = min(1, music_volume + 0.1)
            pygame.mixer.music.set_volume(music_volume)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            music_volume = max(0, music_volume - 0.1)
            pygame.mixer.music.set_volume(music_volume)
        if event.type == pygame.QUIT:
            doing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            state_mode = 1
            all_sprites.update(event)
            if debug:
                for k in all_sprites:
                    print(k.rect.y, k.delta_y)
                print()

    tick.tick(fps)

    screen.blit(fon, (0, 0))  # вывод сурфейса на экран
    all_sprites.draw(screen)  # вывод комплекта спрайтов на экран

    k = 0
    for toy in all_sprites:
        x = toy.rect.x + toy.rect.width / 2
        y = toy.rect.y
        pygame.draw.line(screen, (0, 0, 180), (x, 0), (x, y))
        co[k] = (x, y)
        k += 1
    if state_mode == 2 and abs(start_time_music - time.time()) > 5:
        state_mode = 1
    if state_mode == 1:
        if Math_line.one_line(co[0][0], co[0][1], co[1][0], co[1][1], co[2][0], co[2][1]) \
                and Math_line.one_line(co[0][0], co[0][1], co[1][0], co[1][1], co[3][0], co[3][1]) \
                and Math_line.one_line(co[0][0], co[0][1], co[1][0], co[1][1], co[4][0], co[4][1]):
            start_time_music = time.time()
            pygame.mixer.music.load(random.choice(["data/d0.mp3", "data/d3.mp3"]))
            pygame.mixer.music.play(-1)
            # pygame.mixer.music.set_volume(0.1)
            state_mode = 2
        elif Math_line.one_line(co[1][0], co[1][1],co[2][0], co[2][1],co[3][0], co[3][1]) \
                and Math_line.one_line(co[1][0], co[1][1], co[2][0], co[2][1], co[4][0], co[4][1])\
                and Math_line.one_line(co[1][0], co[1][1], co[2][0], co[2][1], co[5][0], co[5][1]):
            start_time_music = time.time()
            pygame.mixer.music.load(random.choice(["data/d1.mp3", "data/d4.mp3"]))
            pygame.mixer.music.play(-1)
            # pygame.mixer.music.set_volume(0.1)
            state_mode = 2
        elif Math_line.one_line(co[2][0], co[2][1], co[3][0], co[3][1], co[4][0], co[4][1]) \
                and Math_line.one_line(co[2][0], co[2][1], co[3][0], co[3][1], co[5][0], co[5][1]) \
                and Math_line.one_line(co[2][0], co[2][1], co[3][0], co[3][1], co[6][0], co[6][1]):
            start_time_music = time.time()
            pygame.mixer.music.load(random.choice(["data/d1.mp3", "data/d2.mp3"]))
            pygame.mixer.music.play(-1)
            # pygame.mixer.music.set_volume(0.1)
            state_mode = 2
    screen.blit(decor, (0, 0))
    if state_mode == 2:
        screen.blit(vin, (0, 0))
    pygame.display.flip()
    all_sprites.update()
pygame.quit()
