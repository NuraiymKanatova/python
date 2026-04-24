import pygame
import sys
import random
from pygame.locals import *

pygame.init()

# размеры окна игры
screen_width = 500
screen_height = 600

# скорость кадров
fps = 60

# начальная скорость движения объектов
speed = 5

# скорость игрока
player_speed = 3

# через сколько очков увеличивать скорость врага
speed_up_step = 5
next_speed_up = speed_up_step

# границы дороги
road_left = 120
road_right = 380

# цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# создаем окно игры
displaysurf = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Racer Game")

# загружаем фон дороги
background = pygame.image.load("AnimatedStreet.png")
background = pygame.transform.scale(background, (screen_width, screen_height))

# шрифты для текста
font_small = pygame.font.SysFont("Verdana", 20)
font_large = pygame.font.SysFont("Verdana", 60)

# счетчик собранных монет
coins_collected = 0

# таймер кадров
framepersec = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    # класс игрока
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.image = pygame.transform.scale(self.image, (65, 95))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, 520)
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        # движение игрока влево и вправо по нажатию клавиш
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT] and self.rect.left > road_left:
            self.rect.move_ip(-player_speed, 0)

        if pressed_keys[K_RIGHT] and self.rect.right < road_right:
            self.rect.move_ip(player_speed, 0)


class Enemy(pygame.sprite.Sprite):
    # класс вражеской машины
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.image = pygame.transform.scale(self.image, (80, 110))
        self.rect = self.image.get_rect()     
        self.mask = pygame.mask.from_surface(self.image)
        self.reset_position()

    def reset_position(self):
        # Устанавливаем врага в случайную позицию на дороге выше экрана
        self.rect.center = (
            random.randint(road_left + 40, road_right - 40), 
            -120
        )

    def move(self):
        # враг движется вниз
        self.rect.move_ip(0, speed)

        # если враг уехал за экран, возвращаем его наверх 
        if self.rect.top > screen_height:
            self.reset_position()

class Coin(pygame.sprite.Sprite):
    # класс монеты
    def __init__(self):
        super().__init__()

        # случайный вес монеты
        self.weight = random.choice([1, 2, 3])

        # размер монеты зависит от веса
        size = 25 + self.weight * 5

        self.image = pygame.image.load("Coin.png")
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.reset_position()

    def reset_position(self):
        while True:
            x = random.randint(road_left + 25, road_right - 25)
            y = -30

            self.rect.center = (x, y)

            # если НЕ пересекается с врагом — ок
            if not pygame.sprite.spritecollideany(self, enemies, pygame.sprite.collide_mask):
                break

    def move(self):
        # монета движется вниз
        self.rect.move_ip(0, speed)

        # если монета ушла за экран, удаляем ее
        if self.rect.top > screen_height:
            self.kill()

def game_over():
    # функция завершения игры
    over_text = font_large.render("Game Over", True, black)
    displaysurf.fill(red)
    displaysurf.blit(
        over_text,
        (
            screen_width / 2 - over_text.get_width() / 2,
            screen_height / 2 - over_text.get_height() / 2
        )
    )
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

# создаем объекты игрока и врага
p1 = Player()
e1 = Enemy()

# группы спрайтов
enemies = pygame.sprite.Group()
enemies.add(e1)

coins = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(e1)

# событие появления монет
spawn_coin = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_coin, 1500)

# основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # создаем монеты, если их меньше трех
        if event.type == spawn_coin and len(coins) < 3:
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)

    # фон
    displaysurf.blit(background, (0, 0))

    # счет
    coins_text = font_small.render(f"Coins: {coins_collected}", True, black)
    displaysurf.blit(coins_text, (screen_width - coins_text.get_width() - 10, 10))

    # скорость
    speed_text = font_small.render(f"Speed: {int(speed)}", True, black)
    displaysurf.blit(speed_text, (10, 10))

    # движение и отрисовка
    for entity in all_sprites:
        displaysurf.blit(entity.image, entity.rect)
        entity.move()

    # сбор монет
    collected = pygame.sprite.spritecollide(
        p1,
        coins,
        True,
        pygame.sprite.collide_mask
    )

    if collected:
        for coin in collected:
            coins_collected += coin.weight

    # увеличение скорости врага после N монет
    if coins_collected >= next_speed_up:
        speed += 1
        next_speed_up += speed_up_step

    # столкновение с врагом
    if pygame.sprite.spritecollide(
        p1,
        enemies,
        False,
        pygame.sprite.collide_mask
    ):
        game_over()

    pygame.display.update()
    framepersec.tick(fps)