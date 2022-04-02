# -*- coding utf-8 -*_
import pygame

pygmae.init()
screen  = pygame.display.set_mode((600, 800))
clock = pygame.time.clock

while True:
    screen.fill((0, 0 ,0))

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break


    pygame.display.update()
    clock.tick(30)

pygame.quit()