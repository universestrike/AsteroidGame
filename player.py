import pygame
from constants import *
class Player:
    
    rotation = 0

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS):
        self.position = pygame.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.radius = PLAYER_RADIUS
        self.color = (255, 255, 255)

    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, surface):
        pygame.draw.polygon(surface, self.color,self.triangle(),2)
