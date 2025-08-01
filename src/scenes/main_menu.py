
import pygame
from src.scenes.scene import Scene
from src.utils.settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK

class MainMenuScene(Scene):
    def __init__(self):
        super().__init__()
        self.next_scene = None
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 50)

        self.title_text = self.font.render("ARMOR", True, WHITE)
        self.title_rect = self.title_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100))

        self.new_game_text = self.small_font.render("New Game", True, WHITE)
        self.new_game_rect = self.new_game_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

        self.options_text = self.small_font.render("Options", True, WHITE)
        self.options_rect = self.options_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50))

        self.quit_text = self.small_font.render("Quit", True, WHITE)
        self.quit_rect = self.quit_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.new_game_rect.collidepoint(event.pos):
                    from src.scenes.character_creation import CharacterCreationScene
                    self.next_scene = CharacterCreationScene()
                elif self.options_rect.collidepoint(event.pos):
                    # Placeholder for switching to the options scene
                    print("Options clicked")
                elif self.quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    quit()

    def draw(self, screen):
        screen.fill(BLACK)
        screen.blit(self.title_text, self.title_rect)
        screen.blit(self.new_game_text, self.new_game_rect)
        screen.blit(self.options_text, self.options_rect)
        screen.blit(self.quit_text, self.quit_rect)
