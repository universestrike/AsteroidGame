import pygame
from constants import *
from circleshape import CircleShape
from shot import *
class Player(CircleShape):
    

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_RADIUS)
        self.color = (255, 255, 255)
        self.rotation = 0
        self.thrusting = False
        self.shotcd = 0

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

        #movement
        if keys[pygame.K_a]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED * dt
        if keys[pygame.K_w]:
            self.thrusting = True
        else:
            self.thrusting = False
        
        #shot timer
        if self.shotcd > 0:
            self.shotcd-= dt
        
        self.move(dt)

    def move(self, dt):
        self.update_direction()
        if self.thrusting:
            self.velocity += self.forward * PLAYER_SPEED * dt
        self.position += self.velocity * dt

        damping = .98
        self.velocity *= damping

        self.position.x = max(self.radius, min(self.position.x, SCREEN_WIDTH - self.radius))
        self.position.y = max(self.radius, min(self.position.y, SCREEN_HEIGHT - self.radius))

    def shoot(self):
        if self.shotcd <= 0:
            Shot(self.position + self.forward * self.radius, self.forward)
            self.shotcd = PLAYER_SHOOT_COOLDOWN
        