import pygame
import sys

# 파이게임 초기화
pygame.init()

# 화면 크기 설정
screen_size = (1024, 1024)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("1024x1024 정사각형 화면")

# 이미지 경로 설정 (이 부분을 실제 이미지 파일 경로로 바꿔주세요)
image_path = "ai_project/storytelling/image/01.png"

try:
    # 이미지 불러오기
    image = pygame.image.load(image_path)

    # 이미지 크기 설정
    image = pygame.transform.scale(image, (screen_size[0], screen_size[1]))

except pygame.error as e:
    print("이미지를 불러오는 데 오류가 발생했습니다:", e)
    sys.exit()

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 화면에 이미지 표시
    screen.blit(image, (0, 0))

    # 화면 업데이트
    pygame.display.flip()

    # 초당 프레임 수 설정
    pygame.time.Clock().tick(60)
