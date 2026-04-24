import pygame
import sys
import math

pygame.init()

# размеры окна
width, height = 900, 650
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mini Paint Practice 11")

# цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
yellow = (255, 220, 0)
gray = (220, 220, 220)

# настройки
current_color = black
mode = "rect"
drawing = False
start_pos = None
line_width = 3

font = pygame.font.SysFont("Verdana", 16)

canvas = pygame.Surface((width, height))
canvas.fill(white)

clock = pygame.time.Clock()


def draw_menu():
    pygame.draw.rect(screen, gray, (0, 0, width, 60))

    text1 = font.render(
        "R-Rect | C-Circle | S-Square | T-Right Triangle | Q-Equilateral Triangle | D-Diamond | E-Eraser",
        True,
        black
    )
    text2 = font.render(
        "1-Black | 2-Red | 3-Green | 4-Blue | 5-Yellow",
        True,
        black
    )

    screen.blit(text1, (10, 8))
    screen.blit(text2, (10, 32))

    pygame.draw.rect(screen, current_color, (840, 15, 30, 30))


def get_rect_points(start, end):
    x1, y1 = start
    x2, y2 = end

    left = min(x1, x2)
    right = max(x1, x2)
    top = min(y1, y2)
    bottom = max(y1, y2)

    return left, top, right, bottom


def draw_rectangle(surface, start, end, color):
    left, top, right, bottom = get_rect_points(start, end)
    pygame.draw.rect(surface, color, (left, top, right - left, bottom - top), line_width)


def draw_circle(surface, start, end, color):
    radius = int(math.dist(start, end))
    pygame.draw.circle(surface, color, start, radius, line_width)


def draw_square(surface, start, end, color):
    x1, y1 = start
    x2, y2 = end

    side = min(abs(x2 - x1), abs(y2 - y1))

    if x2 < x1:
        x = x1 - side
    else:
        x = x1

    if y2 < y1:
        y = y1 - side
    else:
        y = y1

    pygame.draw.rect(surface, color, (x, y, side, side), line_width)


def draw_right_triangle(surface, start, end, color):
    left, top, right, bottom = get_rect_points(start, end)

    points = [
        (left, top),
        (left, bottom),
        (right, bottom)
    ]

    pygame.draw.polygon(surface, color, points, line_width)


def draw_equilateral_triangle(surface, start, end, color):
    left, top, right, bottom = get_rect_points(start, end)

    side = right - left
    height_triangle = int(side * math.sqrt(3) / 2)

    if bottom - top < height_triangle:
        height_triangle = bottom - top
        side = int(height_triangle * 2 / math.sqrt(3))

    center_x = (left + right) // 2

    points = [
        (center_x, top),
        (center_x - side // 2, top + height_triangle),
        (center_x + side // 2, top + height_triangle)
    ]

    pygame.draw.polygon(surface, color, points, line_width)


def draw_diamond(surface, start, end, color):
    left, top, right, bottom = get_rect_points(start, end)

    center_x = (left + right) // 2
    center_y = (top + bottom) // 2

    points = [
        (center_x, top),
        (right, center_y),
        (center_x, bottom),
        (left, center_y)
    ]

    pygame.draw.polygon(surface, color, points, line_width)


def draw_shape(surface, start, end, color):
    if mode == "rect":
        draw_rectangle(surface, start, end, color)
    elif mode == "circle":
        draw_circle(surface, start, end, color)
    elif mode == "square":
        draw_square(surface, start, end, color)
    elif mode == "right_triangle":
        draw_right_triangle(surface, start, end, color)
    elif mode == "equilateral_triangle":
        draw_equilateral_triangle(surface, start, end, color)
    elif mode == "diamond":
        draw_diamond(surface, start, end, color)


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
            elif event.key == pygame.K_s:
                mode = "square"
            elif event.key == pygame.K_t:
                mode = "right_triangle"
            elif event.key == pygame.K_q:
                mode = "equilateral_triangle"
            elif event.key == pygame.K_d:
                mode = "diamond"
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
            if event.pos[1] > 60:
                drawing = True
                start_pos = event.pos

        # ластик
        if event.type == pygame.MOUSEMOTION:
            if drawing and mode == "eraser":
                pygame.draw.circle(canvas, white, event.pos, 18)

        # конец рисования
        if event.type == pygame.MOUSEBUTTONUP:
            if drawing and start_pos is not None:
                end_pos = event.pos

                if mode != "eraser":
                    draw_shape(canvas, start_pos, end_pos, current_color)

                drawing = False
                start_pos = None

    # основное полотно
    screen.blit(canvas, (0, 0))

    # preview фигуры во время рисования
    if drawing and start_pos is not None and mode != "eraser":
        draw_shape(screen, start_pos, mouse_pos, current_color)

    # меню сверху
    draw_menu()

    pygame.display.update()
    clock.tick(60)