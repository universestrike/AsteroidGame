import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    
    clock = pygame.time.Clock()
    pygame.font.init()
    font = pygame.font.SysFont(None, 72)

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (updatables, drawables)

    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
    asteroidfield = AsteroidField()

    hit_time = None

    game = True
    while game:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        # Only update game objects if player hasn't been hit
        if hit_time is None:
            updatables.update(dt)

            # Collision check
            for sprite in updatables:
                if isinstance(sprite, Asteroid) and player.collision(sprite):
                    print("Player hit!")
                    hit_time = pygame.time.get_ticks()

        # Draw everything
        screen.fill((0, 0, 0))
        for sprite in drawables:
            sprite.draw(screen)

        # If player hit, draw Game Over message
        if hit_time is not None:
            text_surface = font.render("Game Over", True, (255, 0, 0))
            text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text_surface, text_rect)

            # After 5 seconds, quit the game
            if pygame.time.get_ticks() - hit_time >= 5000:
                game = False

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
