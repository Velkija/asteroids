# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	Shot.containers = (shots, updatable, drawable)
	asteroid_field = AsteroidField()
	Player.containers = (updatable, drawable)

	while True:
		for event in pygame.event.get():
   			if event.type == pygame.QUIT:
       				return
		updatable.update(dt)
		for asteroid in asteroids:
			if asteroid.collides_with(player):
				print("Game over!")
				sys.exit()
			for shot in shots:
				if asteroid.collides_with(shot):
					shot.kill()
					asteroid.split()

		screen.fill("black")

		for obj in drawable:
			obj.draw(screen)
		player.draw(screen)
		pygame.display.flip()
		player.update(dt)

		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
