import pygame
import random
import math

# Pygameの初期化
pygame.init()

# 画面の設定
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ボムへいをわけろ！")

# 背景画像の読み込み
background = pygame.image.load("ex05/deta/background.png")

# ボムの設定
bomb_image = pygame.image.load("ex05/deta/bom1.png")
bomb_image = pygame.transform.rotozoom(bomb_image, 0, 0.05)
bomb_rect = bomb_image.get_rect()
bomb_spawn_interval = 3000  # ボムの出現間隔（ミリ秒）
next_bomb_spawn_time = 0

bombs = []
count = 0

# ボムの位置と速度
bomb_x = screen_width // 2 - bomb_rect.width // 2  # 画面の中央部分に配置
bomb_y = 0
while(True):
    c = random.randint(-1, 1)
    if not(c == 0):
        bomb_speed_x = c
        break
while(True):
    b = random.random()
    if not(b == 0):
        bomb_speed_y = b
        break
a = math.sqrt(abs(1/(bomb_speed_x**2)+(bomb_speed_y**2)))
bomb_speed_x = bomb_speed_x * a
bomb_speed_y = bomb_speed_y * a

# 安全地帯の設定
safe_zone1 = pygame.Rect(0,170,214,240)
safe_zone2 = pygame.Rect(555,170,300,240)

# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 背景画像の描画
    screen.blit(background, (0, 0))

    # ボムの描画
    screen.blit(bomb_image, (bomb_x, bomb_y))

    #安全地帯の黄色の枠
    pygame.draw.rect(background,(255,241,0),(555,170,189,240))
    pygame.draw.rect(background,(255,241,0),(24,170,190,240))

    #安全地帯の黒と赤の四角
    pygame.draw.rect(background,(0,0,0),(575,190,170,200))
    pygame.draw.rect(background,(255,0,0),(24,190,169,200))

    # ボムの位置更新
    bomb_x += (bomb_speed_x * 0.1)
    bomb_y += (bomb_speed_y * 0.1)

    # ボムが壁に当たった場合の反射
    if bomb_x < 0 or bomb_x > screen_width - bomb_rect.width:
        bomb_speed_x *= -1
    if bomb_y < 0 or bomb_y > screen_height - bomb_rect.height:
        bomb_speed_y *= -1

    # 安全地帯の範囲内かどうかをチェック
    if safe_zone1.collidepoint(bomb_x, bomb_y):
        # 安全地帯内にボムが入ったら反射
        if bomb_x < safe_zone1.right:
            bomb_speed_x *= -1
        elif bomb_y > safe_zone1.top or bomb_y < safe_zone1.bottom:
            bomb_speed_y *= -1
    if safe_zone2.collidepoint(bomb_x, bomb_y):
        if bomb_x > safe_zone2.left:
            bomb_speed_x *= -1
        elif bomb_y > safe_zone2.top:
            bomb_speed_y *= -1

    # 画面更新
    pygame.display.update()

# Pygameの終了
pygame.quit()