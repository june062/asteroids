import pygame
import sys
from constants import * 
from player import *
from asteroid import *
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()
    Shot.containers = (shots,updatables,drawables)
    


    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables
    asteroid_field = AsteroidField()

    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    clock = pygame.time.Clock()
    dt = 0

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60) / 1000
        screen.fill((0,0,0))
        updatables.update(dt)

        for asteroid in asteroids:
            if asteroid.check_for_collisions(player):
                
                sys.exit("Game over!")

            for asteroid in asteroids:
                for shot in shots:
                    if asteroid.check_for_collisions(shot):
                        asteroid.split()
                        shot.kill()

        for drawable in drawables:
            drawable.draw(screen)
        
        pygame.display.flip()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")





if __name__ == "__main__":
    main()