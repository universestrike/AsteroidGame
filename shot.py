from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, start_position, direction):
        super().__init__(start_position.x, start_position.y, SHOT_RADIUS)
        self.color = (255,255,255)
        self.velocity = direction * PLAYER_SHOOT_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)


    def update(self, dt):
        self.position+=self.velocity * dt
        self.lifetime -= dt
        if (self.position.x < -self.radius or self.position.x > SCREEN_WIDTH + self.radius or
            self.position.y < -self.radius or self.position.y > SCREEN_HEIGHT + self.radius):
            self.kill()