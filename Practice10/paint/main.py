import pygame
import sys
import math

pygame.init()

# размеры окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mini Paint")

# цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
yellow = (255, 220, 0)
gray = (220, 220, 220)

# текущие настройки
current_color = black
mode = "rect"
drawing = False
start_pos = None

# толщина линии (НОВОЕ)
line_width = 3

# шрифты
font = pygame.font.SysFont("Verdana", 18)

# полотно
canvas = pygame.Surface((width, height))
canvas.fill(white)

clock = pygame.time.Clock()


def draw_menu():
    pygame.draw.rect(screen, gray, (0, 0, width, 40))

    text = font.render(
        "R-Rect | C-Circle | E-Eraser | 1-Black 2-Red 3-Green 4-Blue 5-Yellow",
        True,
        black
    )
    screen.blit(text, (10, 10))

    pygame.draw.rect(screen, current_color, (740, 8, 25, 25))


def draw_rectangle(surface, start, end, color):
    x = min(start[0], end[0])
    y = min(start[1], end[1])
    w = abs(end[0] - start[0])
    h = abs(end[1] - start[1])

    pygame.draw.rect(surface, color, (x, y, w, h), line_width)


def draw_circle(surface, start, end, color):
    radius = int(math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2))
    pygame.draw.circle(surface, color, start, radius, line_width)


while True:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # выбор инструмента и цвета
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rect"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_e:
                mode = "eraser"

            elif event.key == pygame.K_1:
                current_color = black
            elif event.key == pygame.K_2:
                current_color = red
            elif event.key == pygame.K_3:
                current_color = green
            elif event.key == pygame.K_4:
                current_color = blue
            elif event.key == pygame.K_5:
                current_color = yellow

        # начало рисования
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[1] > 40:
                drawing = True
                start_pos = event.pos

        # ластик
        if event.type == pygame.MOUSEMOTION:
            if drawing and mode == "eraser":
                pygame.draw.circle(canvas, white, event.pos, 15)

        # завершение рисования
        if event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                end_pos = event.pos

                if mode == "rect":
                    draw_rectangle(canvas, start_pos, end_pos, current_color)

                elif mode == "circle":
                    draw_circle(canvas, start_pos, end_pos, current_color)

                drawing = False
                start_pos = None

    # отображение полотна
    screen.blit(canvas, (0, 0))

    # превью
    if drawing and start_pos is not None:
        if mode == "rect":
            draw_rectangle(screen, start_pos, mouse_pos, current_color)
        elif mode == "circle":
            draw_circle(screen, start_pos, mouse_pos, current_color)

    # меню
    draw_menu()

    pygame.display.update()
    clock.tick(60)