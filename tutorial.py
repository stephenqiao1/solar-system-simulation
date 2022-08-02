import pygame
import math
pygame.init()

# variables/constants
WIDTH, HEIGHT = 1600, 800

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
AMBER = (255, 191, 0)

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Solar System Simulation')


class Planet:
    # astronomical units in meters
    AU = 149.6e6 * 1000
    # gravitational acceleration
    G = 6.67428e-11
    SCALE = 150 / AU # 1 AU = 100 pixels
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

    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10 ** 30)
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10 ** 24)

    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10 ** 23)

    mercury = Planet(-0.387 * Planet.AU, 0, 8, DARK_GREY, 3.30 * 10 ** 23)

    venus = Planet(-0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10 ** 24)

    jupiter = Planet(-5.2 * Planet.AU, 0, 20, AMBER, 1.898 * 10 ** 27)

    planets = [sun, earth, mars, mercury, venus, jupiter]

    while is_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_run = False

        for planet in planets:
            planet.draw(WINDOW)

        pygame.display.update()

    pygame.quit()


main()
