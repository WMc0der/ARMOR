
import pygame
import sys

def create_placeholder_image(file_path, color):
    pygame.init()
    image = pygame.Surface((50, 50))
    image.fill(color)
    pygame.image.save(image, file_path)

if __name__ == "__main__":
    file_path = sys.argv[1]
    color = eval(sys.argv[2])
    create_placeholder_image(file_path, color)
