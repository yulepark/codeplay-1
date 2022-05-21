# -*- coding: utf-8 -*-
import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("똥 피하기 - 코드플레이")

circleX_pos = 0
circleY_pos = 0

clock = pygame.time.Clock()

running = True
while running:
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            #print("mouseMotion")
            #print(pygame.mouse.get_pos())
            circleX_pos, circleY_pos = pygame.mouse.get_pos()
            screen.fill((0, 0, 0))
            pygame.draw.circle(screen, (255, 255, 255), (circleX_pos, circleY_pos), 10)

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("mouseButtonDown")
            #print(pygame.mouse.get_pos)
           # print(event.button)
            #if event.button == 1:
                #print("좌클")
            #elif event.button == 3:
            #    print("우클")
            #elif event.button == 2:
            #    print("휠클")
            #elif event.button == 4:
            #   print("휠업")
            #elif event.button == 5:
            #    print("휠다운")

        if event.type == pygame.MOUSEBUTTONUP:
            print("mouseButtonUp")
            #pass