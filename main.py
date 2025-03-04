# This imports the pygame library and allows us to utilize it
import pygame

# This imports the module for the constants
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *

def main():
    #initializes pygame
    pygame.init()
    
    #restricts fps
    clock = pygame.time.Clock()
    dt = 0

    #groups
    updateable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    Player.containers = (updateable_group, drawable_group)
    Asteroid.containers = (asteroids_group, updateable_group, drawable_group)
    AsteroidField.containers = (updateable_group)

    #basic prints to check run
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #sets screen using pygame display set mode
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Instantiates player object
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2), PLAYER_RADIUS)
    asteroid_field = AsteroidField()
    asteroid_field.__init__()
    #update method
    while(pygame.get_init()):

        
        #makes background
        screen.fill("black")

        #makes close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #draws player on screen
        for thing in drawable_group:
            thing.draw(screen)
        
        updateable_group.update(dt)
        #detects collision
        for asteroid in asteroids_group:
            if asteroid.collision(player):
                print("Game over!")
                return
            
        #ticks clock
        dt = clock.tick(60) / 1000
        
        #calls the update ALWAYS CALL LAST
        pygame.display.flip()


if __name__ == "__main__":
    main()