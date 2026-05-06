import pygame, random
from logger import log_event
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = "white"
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50) 
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)
        old_radius = self.radius
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        child1 = Asteroid(self.position.x, self.position.y, new_radius)
        child2 = Asteroid(self.position.x, self.position.y, new_radius)
        child1.velocity = vector1 * 1.2
        child2.velocity = vector2 * 1.2

