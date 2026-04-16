import pygame
from clock import MickeyClock

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()
mickey = MickeyClock(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    mickey.update()
    mickey.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()