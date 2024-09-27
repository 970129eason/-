import pygame
import sys
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# 初始化Pygame
pygame.init()

# 設置遊戲視窗
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("上傳圖片的遊戲")

# 顏色設置
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 定義角色參數
PLAYER_SIZE = 50
PLAYER_SPEED = 5

# 顯示打開檔案的對話方塊
Tk().withdraw()
filename = askopenfilename(title="選擇背景圖片", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])

if not filename:
    print("未選擇圖片, 程式將退出")
    pygame.quit()
    sys.exit()

# 載入背景圖片
background_image = pygame.image.load(filename)
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

# 創建角色
player_rect = pygame.Rect(WINDOW_WIDTH//2, WINDOW_HEIGHT//2, PLAYER_SIZE, PLAYER_SIZE)

# 主循環
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_rect.move_ip(0, -PLAYER_SPEED)
    if keys[pygame.K_s]:
        player_rect.move_ip(0, PLAYER_SPEED)
    if keys[pygame.K_a]:
        player_rect.move_ip(-PLAYER_SPEED, 0)
    if keys[pygame.K_d]:
        player_rect.move_ip(PLAYER_SPEED, 0)

    # 防止角色移出視窗
    player_rect.clamp_ip(screen.get_rect())

    # 繪製背景
    screen.blit(background_image, (0, 0))

    # 繪製角色
    pygame.draw.rect(screen, RED, player_rect)

    pygame.display.flip()

pygame.quit()
