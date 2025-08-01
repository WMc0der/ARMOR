
import pygame
from src.scenes.scene import Scene
from src.sprites.player import Player
from src.sprites.ant import Ant
from src.sprites.bullet import Bullet
from src.sprites.wall import Wall
from src.sprites.pickups import HealthPickup, Poison
from src.utils.settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK

class GameScene(Scene):
    def __init__(self, selected_character):
        super().__init__()
        self.all_sprites = pygame.sprite.Group()
        self.ants = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.pickups = pygame.sprite.Group()

        self.player = Player(selected_character)
        self.all_sprites.add(self.player)

        self.score = 0
        self.font = pygame.font.Font(None, 36)

        # Create walls
        wall_list = [
            [0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 40],
            [0, 0, 20, SCREEN_HEIGHT],
            [SCREEN_WIDTH - 20, 0, 20, SCREEN_HEIGHT],
            [100, 500, 100, 20],
            [300, 400, 100, 20],
            [500, 300, 100, 20],
        ]

        for item in wall_list:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.walls.add(wall)
            self.all_sprites.add(wall)

        # Create pickups
        health_pickup = HealthPickup(200, 450)
        self.pickups.add(health_pickup)
        self.all_sprites.add(health_pickup)

        poison = Poison(400, 350)
        self.pickups.add(poison)
        self.all_sprites.add(poison)

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

        # Check for collisions between the player and walls
        self.player.rect.x += self.player.change_x
        block_hit_list = pygame.sprite.spritecollide(self.player, self.walls, False)
        for block in block_hit_list:
            if self.player.change_x > 0:
                self.player.rect.right = block.rect.left
            elif self.player.change_x < 0:
                self.player.rect.left = block.rect.right

        self.player.rect.y += self.player.change_y
        block_hit_list = pygame.sprite.spritecollide(self.player, self.walls, False)
        for block in block_hit_list:
            if self.player.change_y > 0:
                self.player.rect.bottom = block.rect.top
            elif self.player.change_y < 0:
                self.player.rect.top = block.rect.bottom
            self.player.change_y = 0

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

        # Check for collisions between the player and pickups
        hits = pygame.sprite.spritecollide(self.player, self.pickups, True)
        for hit in hits:
            if isinstance(hit, HealthPickup):
                self.player.health += 25
                if self.player.health > 100:
                    self.player.health = 100
            elif isinstance(hit, Poison):
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
