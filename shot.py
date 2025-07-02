import pygame
from circleshape import *
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED
from main import *
class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        for group in self.containers:
            group.add(self)



    # This method draws the asteroid on the screen.
    def draw(self, screen):
            pygame.draw.circle(screen, "red", (int(self.position.x), int(self.position.y)), self.radius, 2)

    # This method updates the asteroid's position.
    def update(self, dt):
        moves = (self.velocity * dt)
        self.position = self.position + moves