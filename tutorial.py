import pygame
import math
pygame.init()

# variables/constants
WIDTH, HEIGHT = 800, 800
WHITE = (255, 255, 255)


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Solar System Simulation')


def main():
    is_run = True

    while is_run:
        WINDOW.fill(WHITE)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_run = False

    pygame.quit()


main()
