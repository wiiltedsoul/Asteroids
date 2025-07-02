import pygame
from constants import *
from circleshape import *
import random

# This class represents an asteroid in the game.
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)


    # This method draws the asteroid on the screen.
    def draw(self, screen):
            pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    # This method updates the asteroid's position.
    def update(self, dt):
        moves = (self.velocity * dt)
        self.position = self.position + moves
    
    def xeno(self, target, dt):
         self.kill()
         if self.radius <= ASTEROID_MIN_RADIUS:
              return
         angle = random.uniform(20, 50)
         xeno1 = self.velocity.rotate(angle)
         xeno2 = self.velocity.rotate(-angle)
         xeno_radius = self.radius - ASTEROID_MIN_RADIUS
         asteroid = Asteroid(self.position.x, self.position.y, xeno_radius)
         asteroid.velocity = xeno1 * 1.2
         asteroid = Asteroid(self.position.x, self.position.y, xeno_radius)
         asteroid.velocity = xeno2 * 1.2