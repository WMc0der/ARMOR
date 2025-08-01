
import pygame
from src.scenes.scene import Scene
from src.utils.settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK

class GameOverScene(Scene):
    def __init__(self, score):
        super().__init__()
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 50)

        self.title_text = self.font.render("Game Over", True, WHITE)
        self.title_rect = self.title_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100))

        self.score_text = self.small_font.render(f"Score: {score}", True, WHITE)
        self.score_rect = self.score_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

        self.restart_text = self.small_font.render("Restart", True, WHITE)
        self.restart_rect = self.restart_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100))

        self.quit_text = self.small_font.render("Quit", True, WHITE)
        self.quit_rect = self.quit_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.restart_rect.collidepoint(event.pos):
                    from src.scenes.character_creation import CharacterCreationScene
                    self.next_scene = CharacterCreationScene()
                elif self.quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    quit()

    def draw(self, screen):
        screen.fill(BLACK)
        screen.blit(self.title_text, self.title_rect)
        screen.blit(self.score_text, self.score_rect)
        screen.blit(self.restart_text, self.restart_rect)
        screen.blit(self.quit_text, self.quit_rect)
