import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Call parent constructor
        if hasattr(self, "containers"):
            super().__init__(x, y, radius)
        else:
            super().__init__(x, y, radius)

        self.color = (200, 200, 200)  # light gray

    def draw(self, screen):
        # Draw as a hollow circle (width=2)
        pygame.draw.circle(screen, self.color, self.position, self.radius, width=2)

    def update(self, dt):
        # Move in a straight line at constant speed
        self.position += self.velocity * dt
    