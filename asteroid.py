import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += dt * self.velocity
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20.0,50.0)
        pos_vector = self.velocity.rotate(random_angle)
        neg_vector = self.velocity.rotate(-abs(random_angle))

        old_radius = self.radius
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        
        pos_asteroid = Asteroid(self.position[0],self.position[1], new_radius)
        pos_asteroid.velocity = pos_vector * 1.2
        neg_asteroid = Asteroid(self.position[0],self.position[1], new_radius)
        neg_asteroid.velocity = neg_vector * 1.2