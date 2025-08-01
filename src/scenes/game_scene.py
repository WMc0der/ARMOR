
import pygame
from src.scenes.scene import Scene
from src.sprites.player import Player
from src.sprites.ant import Ant
from src.sprites.bullet import Bullet
from src.utils.settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK

class GameScene(Scene):
    def __init__(self):
        super().__init__()
        self.all_sprites = pygame.sprite.Group()
        self.ants = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self.player = Player()
        self.all_sprites.add(self.player)

        self.score = 0
        self.font = pygame.font.Font(None, 36)

        for _ in range(8):
            ant = Ant()
            self.all_sprites.add(ant)
            self.ants.add(ant)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.shoot()

    def update(self):
        self.all_sprites.update()

        # Check for collisions between bullets and ants
        hits = pygame.sprite.groupcollide(self.ants, self.bullets, True, True)
        for hit in hits:
            self.score += 10
            ant = Ant()
            self.all_sprites.add(ant)
            self.ants.add(ant)

        # Check for collisions between the player and ants
        hits = pygame.sprite.spritecollide(self.player, self.ants, True)
        for hit in hits:
            self.player.health -= 25
            if self.player.health <= 0:
                # Placeholder for game over
                print("Game Over")

    def draw(self, screen):
        screen.fill(BLACK)
        self.all_sprites.draw(screen)

        # Draw the score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Draw the health bar
        health_bar = pygame.Rect(10, 50, self.player.health, 20)
        pygame.draw.rect(screen, (0, 255, 0), health_bar)

    def shoot(self):
        bullet = Bullet(self.player.rect.centerx, self.player.rect.top)
        self.all_sprites.add(bullet)
        self.bullets.add(bullet)
