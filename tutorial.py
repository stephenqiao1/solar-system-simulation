import pygame
import math
pygame.init()

# variables/constants
WIDTH, HEIGHT = 800, 800
WHITE = (255, 255, 255)


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Solar System Simulation')


class Planet:
    # astronomical units in meters
    AU = 149.6e6 * 1000
    # gravitational acceleration
    G = 6.67428e-11
    SCALE = 250 / AU # 1 AU = 100 pixels
    TIMESCALE = 60 * 60 * 24 # 1 day

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT /2
        pygame.draw.circle(win, self.color, (x,y), self.radius)


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
