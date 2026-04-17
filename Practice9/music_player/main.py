import pygame
from player import MusicPlayer

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont("Arial", 30, bold=True)
small_font = pygame.font.SysFont("Arial", 22)

clock = pygame.time.Clock()
player = MusicPlayer()
player.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next_track()
            elif event.key == pygame.K_b:
                player.previous_track()
            elif event.key == pygame.K_q:
                running = False

    screen.fill((30, 30, 30))

    # получаем размеры экрана
    width, height = screen.get_size()

    # тексты
    title_text = font.render("Music Player", True, (255, 255, 255))
    track_text = small_font.render(
        f"Current track: {player.get_current_track_name()}",
        True,
        (220, 220, 220)
    )

    current_pos = player.get_position()
    track_length = player.get_track_length()

    progress_text = small_font.render(
        f"Position: {current_pos}s / {track_length}s",
        True,
        (220, 220, 220)
    )

    controls_text = small_font.render(
        "P - Play | S - Stop | N - Next | B - Previous | Q - Quit",
        True,
        (180, 180, 180)
    )

    # центрирование текста
    title_rect = title_text.get_rect(center=(width // 2, 60))
    track_rect = track_text.get_rect(center=(width // 2, 130))
    progress_rect = progress_text.get_rect(center=(width // 2, 170))
    controls_rect = controls_text.get_rect(center=(width // 2, 340))

    screen.blit(title_text, title_rect)
    screen.blit(track_text, track_rect)
    screen.blit(progress_text, progress_rect)
    screen.blit(controls_text, controls_rect)

    # progress bar (тоже по центру)
    bar_width = 400
    bar_height = 20
    bar_x = (width - bar_width) // 2
    bar_y = (progress_rect.bottom + controls_rect.top) // 2 - bar_height // 2

    pygame.draw.rect(screen, (80, 80, 80), (bar_x, bar_y, bar_width, bar_height))

    if track_length > 0:
        progress_width = int((current_pos / track_length) * bar_width)
        if progress_width > bar_width:
            progress_width = bar_width

        pygame.draw.rect(
            screen,
            (200, 200, 200),
            (bar_x, bar_y, progress_width, bar_height)
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()