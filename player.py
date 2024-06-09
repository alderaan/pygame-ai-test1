import pygame
from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    PLAYER_SPEED,
    PLAYER_COLOR,
    PLAYER_WIDTH,
    PLAYER_HEIGHT,
)
from llm import call_llm


class Player:
    def __init__(self, x, y, health=100):
        self.rect = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.color = PLAYER_COLOR

    def move(self, dt, keys):
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-PLAYER_SPEED * dt, 0)
        elif keys[pygame.K_RIGHT]:
            self.rect.move_ip(PLAYER_SPEED * dt, 0)
        elif keys[pygame.K_UP]:
            self.rect.move_ip(0, -PLAYER_SPEED * dt)
        elif keys[pygame.K_DOWN]:
            self.rect.move_ip(0, PLAYER_SPEED * dt)

        self.check_bounds()

    def check_bounds(self):
        if self.rect.left < 0:
            call_llm()
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def draw(self, screen):
        color = PLAYER_COLOR

        points = [
            (self.rect.left, self.rect.bottom),  # Bottom-left corner
            (self.rect.centerx, self.rect.top),  # Top-center
            (self.rect.right, self.rect.bottom),  # Bottom-right corner
        ]
        pygame.draw.polygon(screen, color, points)

    def update(self, dt, keys):
        self.move(dt, keys)
