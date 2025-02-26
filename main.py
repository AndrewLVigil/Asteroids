# This imports the pygame library and allows us to utilize it
import pygame

# This imports the module for the constants
from constants import *

def main():
    #initializes pygame
    pygame.init()

    #restricts fps
    clock = pygame.time.Clock()
    dt = 0

    #basic prints to check run
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #sets screen using pygame display set mode
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #update method
    while(pygame.get_init()):
        #makes background
        screen.fill("black")

        #makes close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #ticks clock
        dt = clock.tick(60) / 1000
        
        #calls the update ALWAYS CALL LAST
        pygame.display.flip()


if __name__ == "__main__":
    main()