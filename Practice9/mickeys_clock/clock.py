import os
import math
import pygame
from datetime import datetime


class MickeyClock:
    def __init__(self, screen):
        self.screen = screen
        self.center = (300, 300)

        base_dir = os.path.dirname(__file__)
        image_path = os.path.join(base_dir, "images", "mickey_hand.png")

        original = pygame.image.load(image_path).convert_alpha()

        self.minute_hand = pygame.transform.scale(original, (90, 90))
        self.second_hand = pygame.transform.scale(original, (120, 120))

        self.minutes = 0
        self.seconds = 0

        self.font = pygame.font.SysFont("Arial", 28, bold=True)

    def update(self):
        now = datetime.now()
        self.minutes = now.minute
        self.seconds = now.second

    def draw_hand(self, image, angle, pivot, offset):
        rotated_offset = offset.rotate(-angle)
        rotated_image = pygame.transform.rotate(image, angle)

        rect = rotated_image.get_rect(
            center=(pivot[0] + rotated_offset.x, pivot[1] + rotated_offset.y)
        )

        self.screen.blit(rotated_image, rect)

    def draw_numbers(self):
        radius = 125

        for number in range(1, 13):
            angle = math.radians(number * 30 - 90)

            x = self.center[0] + math.cos(angle) * radius
            y = self.center[1] + math.sin(angle) * radius

            text = self.font.render(str(number), True, (220, 220, 220))
            text_rect = text.get_rect(center=(x, y))
            self.screen.blit(text, text_rect)

    def draw_marks(self):
        for i in range(60):
            angle = math.radians(i * 6 - 90)

            if i % 5 == 0:
                inner_radius = 145
                outer_radius = 170
                line_width = 3
            else:
                inner_radius = 155
                outer_radius = 170
                line_width = 1

            x1 = self.center[0] + math.cos(angle) * inner_radius
            y1 = self.center[1] + math.sin(angle) * inner_radius
            x2 = self.center[0] + math.cos(angle) * outer_radius
            y2 = self.center[1] + math.sin(angle) * outer_radius

            pygame.draw.line(
                self.screen,
                (200, 200, 200),
                (x1, y1),
                (x2, y2),
                line_width
            )

    def draw(self):
        pygame.draw.circle(self.screen, (220, 220, 220), self.center, 170, 2)

        self.draw_marks()
        self.draw_numbers()

        minute_angle = -((self.minutes + self.seconds / 60) * 6)
        second_angle = -(self.seconds * 6)

        minute_offset = pygame.math.Vector2(0, -35)
        second_offset = pygame.math.Vector2(0, -45)

        self.draw_hand(self.minute_hand, minute_angle, self.center, minute_offset)
        self.draw_hand(self.second_hand, second_angle, self.center, second_offset)

        # если красная точка не нужна, удали эту строку
        # pygame.draw.circle(self.screen, (255, 0, 0), self.center, 6)