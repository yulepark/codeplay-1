import pygame
import sys
import random
import math

# 초기화
pygame.init()

# 창 크기
window_size = 800
window = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption("크리스마스 카드")

# 이미지 로드 및 크기 조절
background_image = pygame.image.load("ai_project/storytelling/image/05.png")  # 이미지 파일 경로로 바꿔주세요
background_image = pygame.transform.scale(background_image, (window_size, window_size))

snowflake_image = pygame.image.load("ai_project/storytelling/image/snow.png")  # 눈송이 이미지 파일 경로로 바꿔주세요

# 색상 정의
white = (255, 255, 255)

# 눈송이 정보
class Snowflake:
    def __init__(self):
        self.size = random.randint(10, 30)
        self.x = random.randint(0, window_size)
        self.y = -self.size
        self.speed = random.uniform(1, 3)
        self.rotation = random.uniform(0, 360)  # 랜덤한 각도로 설정
        self.rotation_speed = random.uniform(3, 10)  # 초당 3~10도로 설정

    def update(self):
        self.y += self.speed
        self.rotate()

    def rotate(self):
        self.rotation = (self.rotation + self.rotation_speed) % 360

# 눈송이 생성
snowflakes = [Snowflake() for _ in range(50)]  # 눈송이 개수 조절

# 음악 로드
pygame.mixer.init()  # Pygame Mixer 초기화
pygame.mixer.music.load("ai_project/storytelling/image/song.mp3")  # 음악 파일 경로로 바꿔주세요
pygame.mixer.music.set_volume(0.5)  # 볼륨 조절
pygame.mixer.music.play(-1)  # 음악 반복 재생

# 게임 루프
clock = pygame.time.Clock()
running = True
music_paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            music_paused = not music_paused
            if music_paused:
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()
        # 화면 그리기
    window.blit(background_image, (0, 0))

        # 눈송이 그리기
    for snowflake in snowflakes:
        rotated_snowflake = pygame.transform.rotate(pygame.transform.scale(snowflake_image, (snowflake.size, snowflake.size)),
                                                     snowflake.rotation)
        snowflake_rect = rotated_snowflake.get_rect(center=(snowflake.x, int(snowflake.y)))
        window.blit(rotated_snowflake, snowflake_rect.topleft)

            # 눈송이 위치 업데이트
        snowflake.update()
        if snowflake.y > window_size:
            snowflake.y = -snowflake.size
            snowflake.x = random.randint(0, window_size)
            snowflake.rotation = random.uniform(0, 360)  # 랜덤한 각도로 재설정
            snowflake.rotation_speed = 2  # 초당 3~10도로 재설정

    pygame.display.flip()

clock.tick(55)  # 초당 30프레임

pygame.quit()
sys.exit()
