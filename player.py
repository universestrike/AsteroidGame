import pygame
from constants import *
class Player(pygame.sprite.Sprite):
    
    rotation = 0

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.position = pygame.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.radius = PLAYER_RADIUS
        self.color = (255, 255, 255)
        self.velocity = pygame.Vector2(0,0)
        self.thrusting = False

    def update_direction(self):
        self.forward = pygame.Vector2(0, -1).rotate(self.rotation)

    def triangle(self):
        self.update_direction()
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        # Tip / Back Left / Back Right
        a = self.position + self.forward * self.radius
        b = self.position - self.forward * self.radius - right
        c = self.position - self.forward * self.radius + right
        return [a, b, c]
    
    def draw(self, surface):
        pygame.draw.polygon(surface, self.color,self.triangle(),2)

    def update(self, dt):
        self.update_direction()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED * dt
        if keys[pygame.K_w]:
            self.thrusting = True
        else:
            self.thrusting = False

    def move(self, dt):
        self.update_direction()
        if self.thrusting:
            self.velocity += self.forward * PLAYER_SPEED * dt
        self.position += self.velocity * dt