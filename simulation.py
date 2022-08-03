import pygame
import math
pygame.init()

# variables/constants
WIDTH, HEIGHT = 1400, 1000

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
AMBER = (255, 191, 0)

FONT = pygame.font.SysFont("arial", 16)

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Solar System Simulation')


class Planet:
    # astronomical units in meters
    AU = 149.6e6 * 1000
    # gravitational acceleration
    G = 6.67428e-11
    SCALE = 120 / AU # 1 AU = 100 pixels
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

    def draw(self, window):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT /2

        pygame.draw.circle(window, self.color, (x,y), self.radius)

    # the force of attraction between planets
    def attraction(self, other):
        other_x, other_y = other.x, other.y
        # calculate distance by the difference of the two planets
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        # F = (G * mass 1 * mass 2)/ r^2
        force = self.G * self.mass * other.mass / (distance ** 2)
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def new_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESCALE
        self.y_vel += total_fy / self.mass * self.TIMESCALE

        self.x += self.x_vel * self.TIMESCALE
        self.y += self.y_vel * self.TIMESCALE
        self.orbit.append((self.x, self.y))


def main():
    is_run = True

    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10 ** 30)
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10 ** 24)
    # earths velocity around the sun
    earth.y_vel = 29.783 * 1000

    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10 ** 23)
    # mars velocity around the sun
    mars.y_vel = 24.077 * 1000

    mercury = Planet(-0.387 * Planet.AU, 0, 8, DARK_GREY, 3.30 * 10 ** 23)
    # mecury's velocity around the sun
    mercury.y_vel = 47.87 * 1000

    venus = Planet(-0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10 ** 24)
    # venus' velocity around the sun
    venus.y_vel = 35.02 * 1000

    jupiter = Planet(-5.2 * Planet.AU, 0, 20, AMBER, 1.898 * 10 ** 27)
    jupiter.y_vel = 13.07 * 1000

    planets = [sun, earth, mars, mercury, venus, jupiter]

    while is_run:
        WINDOW.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_run = False

        for planet in planets:
            planet.new_position(planets)
            planet.draw(WINDOW)

        pygame.display.update()

    pygame.quit()


main()
