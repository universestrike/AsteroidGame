import pygame
from constants import *
from player import *
from asteroid import *


def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    
    clock = pygame.time.Clock()
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables)
    
    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
    asteroid = Asteroid(SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MAX_RADIUS)




    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game = True
    while game:
        dt = clock.tick(60)/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatables.update(dt)

        # Clear screen
        screen.fill((0,0,0))

        for sprite in drawables:
            sprite.draw(screen)
        
        pygame.display.flip()
        
    pygame.quit()

if __name__ == "__main__":
    main()
