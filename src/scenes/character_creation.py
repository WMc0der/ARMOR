
import pygame
from src.scenes.scene import Scene
from src.utils.settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK

class CharacterCreationScene(Scene):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 50)

        self.title_text = self.font.render("Character Creation", True, WHITE)
        self.title_rect = self.title_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100))

        self.start_text = self.small_font.render("Start Game", True, WHITE)
        self.start_rect = self.start_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

        self.back_text = self.small_font.render("Back", True, WHITE)
        self.back_rect = self.back_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100))

        self.next_scene = None

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_rect.collidepoint(event.pos):
                    from src.scenes.game_scene import GameScene
                    self.next_scene = GameScene()
                elif self.back_rect.collidepoint(event.pos):
                    from src.scenes.main_menu import MainMenuScene
                    self.next_scene = MainMenuScene()

    def draw(self, screen):
        screen.fill(BLACK)
        screen.blit(self.title_text, self.title_rect)
        screen.blit(self.start_text, self.start_rect)
        screen.blit(self.back_text, self.back_rect)
