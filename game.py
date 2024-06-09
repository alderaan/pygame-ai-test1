import pygame
import time
from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ENEMY_SPEED,
    BLACK,
    WHITE,
)
from player import Player


def game_over_screen(screen):
    font = pygame.font.Font(None, 74)
    screen.fill(BLACK)
    text = font.render("Game Over", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(2)


def initialize_game():
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT)
    return player


def run_game():
    pygame.init()
    pygame.display.set_caption("David's Space Invaders")

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True

    while running:
        player = initialize_game()
        game_over = False

        while not game_over:
            dt = clock.tick(60) / 1000  # Convert milliseconds to seconds

            # EVENT HANDLING
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    running = False

            keys = pygame.key.get_pressed()

            # Update player
            player.update(dt, keys)

            # RENDERING
            screen.fill((0, 0, 0))
            player.draw(screen)

            pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    run_game()
