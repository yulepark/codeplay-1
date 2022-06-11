# -*-coding: utf-8 -*-
import pygame
import random

pygame.init()#초기화 (반드시 필요)


screen_width = 640 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 (제목창)
pygame.display.set_caption("벽돌깨기")

#1.막대기 정의
bar_width = 150
bar_height = 25

bar_xPos = screen_width / 2 - bar_width / 2 #스크린 정 가운데
bar_yPos = screen_height - bar_height #스크린 맨 아래

to_x = 0

#2.공 정의
ball_size = 20 #반지름 쓰기

ball_xPos = screen_width / 2 #원은 중심이 위가 아니라 정 가운데이기때문에 width를 뺄 이유 X
ball_yPos = screen_height - bar_height - ball_size # ball_size를 빼는 이유는 공이 막대기보다 위에 올라오기 위해서

ball_rect = pygame.Rect(ball_xPos, ball_yPos, ball_size * 2, ball_size * 2) #공을 따라다니는 투명한 히트박스 만든것
ball_rect.center = (ball_xPos, ball_yPos) #원의 중심은 가운데고 네모의 중심은 왼쪽 위 꼭짓점이기 때문에 판정이 이상해져서 네모의 중심을 옮김.

#3.블록정의
block_width = screen_width / 10 #스크린을 10개의 조각으로 나눠서 블록이 들어갈 공간 마련
block_height = 40

block_xPos = 0
block_yPos = 0

blocks = [[] for i in range(10)] #10개의 빈 리스트 생성. 왼쪽에 있는 [](빈리스트)를 10번 만들어주는것
block_color = [[], [], [], [], [], [], [], [], [], []] #10개의 빈 리스트 생성. 10개의 색깔 리스트를 만듦.

for i in range(10): #j가 3번 돌고나서 +1이 추가됨. 0,0 ->0,1 ->0,2 -> 1,0 -> 1,1 -> 1,2-> 2,0 순서
    for j in range(3): 
        blocks[i].append(pygame.Rect(i*block_width, j*block_height, block_width, block_height)) #네모를 그리기 (위치, 네모의 크기)
        block_color[i].append((random.randrange(256), random.randrange(256), random.randrange(256))) #RGB 3개의 값을 주고 랜덤한 색 입히기

print(blocks) #리스트에 들어간 값 확인([벽돌의 가로위치, 세로위치 + 벽돌의 가로길이, 세로길이] * 30개)
print(block_color) #리스트에 들어간 값 확인(R값, G값, B값 * 30개)
#이벤트 루프 - 종료까지 대기
running = True #실행중인지 확인
while running:
    for event in pygame.event.get(): #카마 이벤트를 지속적으로 체큰
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

    bar_xPos += to_x
    
    
    if bar_xPos < 0:
        bar_xPos = 0
    elif bar_xPos > screen_width - bar_width:
        bar_xPos = screen_width - bar_width
    
                
    
    #배경그리기
    screen.fill((200, 200, 100))
    #막대기 그리기
    pygame.draw.rect(screen, (90, 90, 255), (bar_xPos, bar_yPos, bar_width, bar_height))
    #공 그리기
    pygame.draw.circle(screen, (255, 255, 255), (ball_xPos, ball_yPos), ball_size)

    #벽돌그리기
    for i in range(10):
        for j in range(3):
            pygame.draw.rect(screen, block_color[i][j], blocks[i][j])


    pygame.display.update()
#종료처리
pygame.quit()