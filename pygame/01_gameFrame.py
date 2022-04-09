#-*- coding: utf-8 -*-
import pygame
pygame.init()


screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("똥 피하기 - 코드플레이")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #print("ㅋㅋ 안죽죠?")
            running = False


pygame.quit()


