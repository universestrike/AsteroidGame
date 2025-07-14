import pygame
from constants import *
from player import *



def main():
    game = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = .01
    player_group = pygame.sprite.Group()
    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))
        player.update(dt)
        player.move(dt)
        player.draw(screen)
        
        pygame.display.flip()
        time.tick(60)

if __name__ == "__main__":
    main()
