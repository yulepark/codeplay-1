#-*- coding: utf-8 -*-
import random
import pygame
pygame.init()


game_font = pygame.font.Font(None, 40)

total_time = 0

start_ticks = pygame.time.get_ticks()


enemy_speed = 10
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("똥 피하기 - 코드플레이")

clock = pygame.time.Clock()

character_speed = 1

bg = pygame.image.load("pygame/source/bg.png")

character = pygame.image.load("pygame/source/character.png")
character_size = character.get_rect(). size
character_width = character_size[0]
character_height = character_size[1]
character_xPos = 0
character_yPos = screen_height / 2 - (character_height / 2)

enemy = pygame.image.load
enemy = pygame.image.load("pygame/source/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_xPos = 640 - enemy_width
enemy_yPos = screen_height / 2 - (enemy_height / 2)
to_x = 0
to_y = 0


running = True
while running:
    dt = clock.tick(60)
    #print("fps : " + str(clock.get_fps()))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    
    character_yPos += to_y * dt

    
    if character_yPos < 0:
        character_yPos = 0
    elif character_yPos > screen_height - character_height:
        character_yPos = screen_height - character_height




    
    character_rect = character.get_rect()
    character_rect.left = character_xPos   
    character_rect.top = character_yPos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_xPos
    enemy_rect.top = enemy_yPos


    enemy_xPos -= enemy_speed
    if enemy_xPos < 0:
        enemy_xPos = screen_width - enemy_width
        enemy_yPos = random.randint(0, (screen_width - enemy_width))
        enemy_speed = random.randint(5, 15)


    if character_rect.colliderect(enemy_rect):
        print(" ^ 3 ^ ")
        print("당신의 점슈는 {0}점 입니다.".format(total_time))
        running = False

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(int(total_time + elapsed_time)), False, (0, 0, 0))




    screen.blit(bg, (0, 0))
    screen.blit(character, (character_xPos, character_yPos))
    screen.blit(enemy, (enemy_xPos, enemy_yPos))
    screen.blit(timer , (10, 10))
    pygame.display.update()






pygame.quit()

