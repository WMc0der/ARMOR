
import pygame
from src.scenes.scene import Scene
from src.utils.settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK

class GameScene(Scene):
    def __init__(self):
        super().__init__()
        self.player = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50, 50, 50)

    def handle_events(self, events):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.x -= 5
        if keys[pygame.K_RIGHT]:
            self.player.x += 5

    def draw(self, screen):
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, self.player)
