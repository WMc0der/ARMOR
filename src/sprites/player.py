
import pygame
from src.utils.settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE

class Player(pygame.sprite.Sprite):
    def __init__(self, selected_character):
        super().__init__()
        self.character_images = [
            pygame.image.load("/Users/thele/workspace/github.com/WMc0der/ARMOR/assets/images/player1.png").convert_alpha(),
            pygame.image.load("/Users/thele/workspace/github.com/WMc0der/ARMOR/assets/images/player2.png").convert_alpha(),
            pygame.image.load("/Users/thele/workspace/github.com/WMc0der/ARMOR/assets/images/player3.png").convert_alpha(),
        ]
        self.image = self.character_images[selected_character]
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50))
        self.speed = 5
        self.health = 100

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        return bullet
