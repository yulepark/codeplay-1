# -*-coding: utf-8 -*-
import pygame
import random

pygame.init()#초기화 (반드시 필요)
pygame.font.init()

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
bar_rect = pygame.Rect(bar_xPos, bar_yPos, bar_width, bar_height)
bar_to_X = 0 #막대기의 움직임을 담아놓음
to_x = 0

#2.공 정의
ball_size = 20 #반지름 쓰기

ball_xPos = screen_width / 2 #원은 중심이 위가 아니라 정 가운데이기때문에 width를 뺄 이유 X
ball_yPos = screen_height - bar_height - ball_size # ball_size를 빼는 이유는 공이 막대기보다 위에 올라오기 위해서
ball_rect = pygame.Rect(ball_xPos, ball_yPos, ball_size * 2, ball_size * 2) #공을 따라다니는 투명한 히트박스 만든것
ball_rect.center = (ball_xPos, ball_yPos) #원의 중심은 가운데고 네모의 중심은 왼쪽 위 꼭짓점이기 때문에 판정이 이상해져서 네모의 중심을 옮김.

ball_x_speed = 0.3
ball_y_speed = 0.3

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

#5.점수 계산하기
point = 0

#6.시작시 카운트후 시작
count = True

#7.화면에 글자 출력
def gameText(words): #매개변수로 받는 내용 화면에 출력
    font = pygame.font.SysFont(None, 100) #폰트지정

    text = font.render(words, True, (80, 180, 80)) #글자내용과 색상 지정

    text_width = text.get_rect().size[0] #텍스트 가로세로 크기지정(좌표계산용)
    text_height = text.get_rect().size[1]

    text_xPos = screen_width / 2 - text_width / 2 #텍스트 위치 지정
    text_yPos = screen_height / 2 - text_height / 2

    screen.blit(text, (text_xPos, text_yPos)) #화면에 텍스트 갱신



#이벤트 루프 - 종료까지 대기
running = True #실행중인지 확인
while running:
    if count:
        count = False
        for i in range(3, 0, -1):
            screen.fill((0, 0, 0))
            gameText(str(i))
            pygame.display.update()
            pygame.time.delay(1000)
        screen.fill((0, 0, 0))
        gameText("Go!")
        pygame.display.update()
        pygame.time.delay(1000) #1초마다 실행
    
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
    bar_xPos += bar_to_X
    if bar_xPos < 0:
        bar_xPos = 0
    if bar_xPos > screen_width - bar_width:
        bar_xPos = screen_width - bar_width
    bar_rect.left = bar_xPos
    
    pygame.draw.rect(screen, (90, 90, 255), bar_rect)
    #공 튕기기
    if ball_xPos - ball_size <= 0:
        ball_x_speed = -ball_x_speed
    elif ball_xPos >= screen_width - ball_size:
        ball_x_speed = -ball_x_speed

    if ball_yPos - ball_size <=0:
        ball_y_speed = -ball_y_speed
    elif ball_yPos >= screen_height: #바닥에 공이닿으면 끝
        #ball_y_speed = -ball_y_speed
        screen.fill((0, 0, 0))
        gameText("Your Score : %d" % point)
        pygame.display.update()
        pygame.time.delay(2000)
        running = False#while 반복문 종료    
    ball_xPos += ball_x_speed
    ball_yPos += ball_y_speed
    
    #공 그리기
    ball_rect.center = (ball_xPos, ball_yPos)
    pygame.draw.circle(screen, (255, 255, 255), (ball_xPos, ball_yPos), ball_size)

    # 충돌판정 : 막대기와 충돌
    if ball_rect.colliderect(bar_rect) :
        ball_y_speed = -ball_y_speed

    #벽돌그리기
    for i in range(10):
        for j in range(3):
            if blocks [i][j]: #벽을 그릴지 말지 결정
                pygame.draw.rect(screen, block_color[i][j], blocks[i][j])
                blocks[i][j].topleft = (i * block_width, j * block_height)

                if ball_rect.colliderect(blocks[i][j]):
                    ball_x_speed *= -1
                    ball_y_speed *= -1
                    blocks[i][j] = 0 #블럭의 정보를 삭제
                    point += 1#블럭을 깰 때마다 점수 1점씩 추가                    
    
    if point >= 30:
        screen.fill((0, 255, 0))
        gameText('Cleared in %d"' % timer)
        pygame.display.update()
        pygame.time.delay(2000)
        running = False
    
    tiemr = pygame.time.get_ticks() / 1000
    
    
    pygame.display.update()
#종료처리
pygame.quit()