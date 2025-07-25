import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0

	updateable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()


	Player.containers = (updateable, drawable)
	Asteroid.containers = (asteroids, updateable, drawable)
	AsteroidField.containers = (updateable)
	Shot.containers = (shots, updateable, drawable)
	

	asteroid_fields = AsteroidField()


	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)



	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		updateable.update(dt)
		shots.update(dt)


		for asteroid in asteroids:
			if asteroid.collisions(player):
				print("Game Over!")
				sys.exit()
				
			for shot in shots:
				if shot.collisions(asteroid):
					shot.kill()
					asteroid.split()

		screen.fill("black")

		for sprite in drawable:
			sprite.draw(screen)
		
		
		pygame.display.flip()

		dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
    