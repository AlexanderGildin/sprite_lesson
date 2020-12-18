# VCS → Import into Version Control → Create Git Repository

# загруженные изображения — это, фактически, обычный Surface
image = pygame.Surface([100, 100])
image.fill(pygame.Color("red"))
...
screen.blit(image, (10, 10))

import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()

if colorkey is not None:
    if colorkey == -1:
        colorkey = image.get_at((0, 0))
    image.set_colorkey(colorkey)
else:
    image = image.convert_alpha()
return image

# создадим группу, содержащую все спрайты
all_sprites = pygame.sprite.Group()

# создадим спрайт
sprite = pygame.sprite.Sprite()
# определим его вид
sprite.image = load_image("bomb.png")
# и размеры
sprite.rect = sprite.image.get_rect()
# добавим спрайт в группу
all_sprites.add(sprite)

# изображение должно лежать в папке data
bomb_image = load_image("bomb.png")

for i in range(50):
    # можно сразу создавать спрайты с указанием группы
    bomb = pygame.sprite.Sprite(all_sprites)
    bomb.image = bomb_image
    bomb.rect = bomb.image.get_rect()

    # задаём случайное местоположение бомбочке
    bomb.rect.x = random.randrange(width)
    bomb.rect.y = random.randrange(height)

# в главном игровом цикле
all_sprites.draw(screen)

