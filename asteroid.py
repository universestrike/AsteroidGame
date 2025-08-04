import pygame
import random
import math
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
    
    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            new_radius = self.radius // 2
            print("Splitting Hit Asteroid into 2 halves.")
            for angle_offset in [random.randint(20,50), -random.randint(20,50)]:
                new_velocity = self.velocity.rotate(angle_offset)
                Asteroid(self.position.x, self.position.y, new_radius).velocity = new_velocity
