
import pygame
import random
from src.utils.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Ant(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))  # Red ant
        self.rect = self.image.get_rect(
            center=(
                random.randint(0, SCREEN_WIDTH),
                random.randint(-100, -40),
            )
        )
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
