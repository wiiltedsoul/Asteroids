# this allows us to use code from
# the open-source pygame library
# throughout this file
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()
        tick = clock.tick(60)
        
        dt = tick / 1000.0



    

if __name__ == "__main__":
    main()