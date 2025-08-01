
import pygame
from src.scenes.scene import Scene
from src.utils.settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK

class CharacterCreationScene(Scene):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 50)

        self.title_text = self.font.render("Character Creation", True, WHITE)
        self.title_rect = self.title_text.get_rect(center=(SCREEN_WIDTH / 2, 100))

        self.character_images = [
            pygame.image.load("/Users/thele/workspace/github.com/WMc0der/ARMOR/assets/images/player1.png").convert_alpha(),
            pygame.image.load("/Users/thele/workspace/github.com/WMc0der/ARMOR/assets/images/player2.png").convert_alpha(),
            pygame.image.load("/Users/thele/workspace/github.com/WMc0der/ARMOR/assets/images/player3.png").convert_alpha(),
        ]

        self.character_rects = []
        for i, image in enumerate(self.character_images):
            rect = image.get_rect(center=(SCREEN_WIDTH / 2 - 200 + (i * 200), SCREEN_HEIGHT / 2))
            self.character_rects.append(rect)

        self.selected_character = None

        self.start_text = self.small_font.render("Start Game", True, WHITE)
        self.start_rect = self.start_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(self.character_rects):
                    if rect.collidepoint(event.pos):
                        self.selected_character = i
                if self.start_rect.collidepoint(event.pos) and self.selected_character is not None:
                    from src.scenes.game_scene import GameScene
                    self.next_scene = GameScene(self.selected_character)

    def draw(self, screen):
        screen.fill(BLACK)
        screen.blit(self.title_text, self.title_rect)

        for i, image in enumerate(self.character_images):
            screen.blit(image, self.character_rects[i])
            if i == self.selected_character:
                pygame.draw.rect(screen, WHITE, self.character_rects[i], 2)

        screen.blit(self.start_text, self.start_rect)
