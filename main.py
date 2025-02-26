# This imports the pygame library and allows us to utilize it
import pygame

# This imports the module for the constants
from constants import *

def main():
    #initializes pygame
    pygame.init()

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #calls the update ALWAYS CALL LAST
        pygame.display.flip()


if __name__ == "__main__":
    main()