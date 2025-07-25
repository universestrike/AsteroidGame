import pygame
from constants import *
from player import *



def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    
    clock = pygame.time.Clock()
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
    updatables.add(player)
    drawables.add(player)

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
