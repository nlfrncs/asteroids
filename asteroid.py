import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        if Asteroid.containers:
            for container in Asteroid.containers:
                container.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            split1_velocity = self.velocity.rotate(angle)
            split2_velocity = self.velocity.rotate(-angle)
            split_radius = self.radius - ASTEROID_MIN_RADIUS

            split1 = Asteroid(self.position.x, self.position.y, split_radius)
            split1.velocity = split1_velocity * 1.2

            split2 = Asteroid(self.position.x, self.position.y, split_radius)
            split2.velocity = split2_velocity * 1.2
