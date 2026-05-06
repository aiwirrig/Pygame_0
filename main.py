import pygame 
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
import sys


def main():
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    player1 = Player(x, y)
    asteroidsfield1 = AsteroidField()



    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for obj in asteroids:
            if obj.collides_with(player1):
                log_event("player_hit")
                obj.split()
                player1.lives -= 1
                player1.position = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                if player1.lives == 0:
                    print("Game Over")
                    sys.exit()
            for bullet in shots:
                if obj.collides_with(bullet):
                    log_event("asteroid_shot")
                    obj.split()
                    pygame.sprite.Sprite.kill(bullet)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        time_added = clock.tick(60)
        dt = time_added / 1000

if __name__ == "__main__":
    main()
