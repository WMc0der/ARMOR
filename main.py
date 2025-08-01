
import pygame
from src.utils.settings import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK
from src.scenes.main_menu import MainMenuScene

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("ARMOR")
    clock = pygame.time.Clock()

    current_scene = MainMenuScene()

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if current_scene.next_scene:
            current_scene = current_scene.next_scene

        current_scene.handle_events(events)
        current_scene.update()
        current_scene.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
