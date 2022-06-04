#-*- coding: utf-8 -*-
import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("똥 피하기 - 코드플레이")

stick = pygame.image.load("pygame/source/stick.png")
stick_size = stick.get_rect(). size
stick_width = stick_size[0]
stick_height = stick_size[1]
stick_xPos = (screen_width / 2) - (stick_width / 2)
stick_yPos = screen_height - stick_height

to_x = 0


ball = pygame.image.load("pygame/source/ball.png")
ball_size = ball.get_rect(). size
ball_width = ball_size[0]
ball_height = ball_size[1]
ball_xPos = (screen_width / 2) - (ball_width / 2)
ball_yPos = screen_height - ball_height

ball_speed_x = 3
ball_speed_y = 3

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 1
            elif event.key == pygame.K_RIGHT:
                to_x += 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
                
    stick_xPos += to_x
    # stick_yPos += to_y
    
    
    if stick_xPos < 0:
        stick_xPos = 0
    elif stick_xPos > screen_width - stick_width:
        stick_xPos = screen_width - stick_width
    
    ball_xPos += ball_speed_x
    ball_yPos += ball_speed_y

    if ball_xPos <= 0:
        ball_speed_x *= -1
        ball_speed_x = 1
    elif ball_xPos >= screen_width - ball_width:
        ball_speed_x *= -1
        ball_speed_x = -1
    if ball_yPos <= 0:
        ball_speed_y *= -1
        ball_speed_y = 1
    elif ball_yPos >= screen_height - ball_height:
        ball_speed_y *= -1
        ball_speed_y = -1



 
    screen.blit(stick, (stick_xPos, stick_yPos))
    screen.blit(ball, (ball_xPos, ball_yPos))

    pygame.display.update()
pygame.quit()

