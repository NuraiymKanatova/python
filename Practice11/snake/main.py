import pygame
import sys
import random

pygame.init()

# размеры окна
width = 600
height = 420

# верхняя панель для текста
top_panel = 40

# размер клетки
block_size = 20

# цвета
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 200, 0)
red = (220, 0, 0)
orange = (255, 140, 0)
purple = (160, 32, 240)
gray = (220, 220, 220)

# окно игры
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# шрифты
font = pygame.font.SysFont("Verdana", 20)
large_font = pygame.font.SysFont("Verdana", 50)

# таймер кадров
clock = pygame.time.Clock()

# время жизни еды
food_lifetime = 7000


def generate_food(snake):
    # создаем еду не у краев, не в зоне текста и не внутри змейки
    margin = block_size * 2

    while True:
        food_x = random.randrange(margin, width - margin, block_size)
        food_y = random.randrange(top_panel + margin, height - margin, block_size)

        if [food_x, food_y] not in snake:
            weight = random.choice([1, 2, 3])

            return {
                "position": [food_x, food_y],
                "weight": weight,
                "created_time": pygame.time.get_ticks()
            }


def draw_food(food):
    # цвет еды зависит от веса
    if food["weight"] == 1:
        color = red
    elif food["weight"] == 2:
        color = orange
    else:
        color = purple

    x, y = food["position"]
    pygame.draw.rect(screen, color, (x, y, block_size, block_size))


def show_score(score, level):
    # показываем счет и уровень
    text = font.render(f"Score: {score}  Level: {level}", True, black)
    screen.blit(text, (10, 8))


def game_over():
    # экран завершения игры
    screen.fill(red)

    text = large_font.render("Game Over", True, black)
    screen.blit(
        text,
        (
            width / 2 - text.get_width() / 2,
            height / 2 - text.get_height() / 2
        )
    )

    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()


def main():
    # начальная позиция змейки
    snake_x = width // 2
    snake_y = top_panel + 160

    # направление движения
    dx = block_size
    dy = 0

    # тело змейки
    snake = [[snake_x, snake_y]]

    # длина змейки
    snake_length = 1

    # счет и уровень
    score = 0
    level = 1

    # скорость
    speed = 6

    # первая еда
    food = generate_food(snake)

    # основной игровой цикл
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # управление
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -block_size
                    dy = 0

                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = block_size
                    dy = 0

                elif event.key == pygame.K_UP and dy == 0:
                    dx = 0
                    dy = -block_size

                elif event.key == pygame.K_DOWN and dy == 0:
                    dx = 0
                    dy = block_size

        # если время еды закончилось, просто создаем новую еду
        current_time = pygame.time.get_ticks()
        if current_time - food["created_time"] > food_lifetime:
            food = generate_food(snake)

        # движение змейки
        snake_x += dx
        snake_y += dy

        # проверка столкновения со стенами
        if snake_x < 0 or snake_x >= width or snake_y < top_panel or snake_y >= height:
            game_over()

        # новая голова змейки
        snake_head = [snake_x, snake_y]
        snake.append(snake_head)

        # удаляем хвост, если длина больше нужной
        if len(snake) > snake_length:
            del snake[0]

        # проверка столкновения с самой собой
        if snake_head in snake[:-1]:
            game_over()

        # проверка поедания еды
        if snake_head == food["position"]:
            score += food["weight"]
            snake_length += food["weight"]

            level = score // 4 + 1
            speed = min(6 + level, 12)

            food = generate_food(snake)

        # фон
        screen.fill(white)

        # сетка
        for x in range(0, width, block_size):
            for y in range(top_panel, height, block_size):
                pygame.draw.rect(screen, gray, (x, y, block_size, block_size), 1)

        # еда
        draw_food(food)

        # змейка
        for part in snake:
            pygame.draw.rect(screen, green, (part[0], part[1], block_size, block_size))

        # счет и уровень
        show_score(score, level)

        pygame.display.update()
        clock.tick(speed)


main()