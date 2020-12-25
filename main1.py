import pygame
import os

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
a = input().split()
b = input().split()

if __name__ == '__main__':
    pygame.init()
    bg = pygame.Surface((WIDTH, HEIGHT))
    bg.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 0, 255), (250 + int(a[0]), 250 + int(a[1]), int(a[2]), int(a[3])),
                     1)
    pygame.draw.rect(screen, (0, 0, 255), (250 + int(b[0]), 250 + int(b[1]), int(b[2]), int(b[3])),
                     1)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
