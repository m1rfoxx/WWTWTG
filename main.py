import pygame
import sys
import random

pygame.init()

# Параметры окна
WIDTH, HEIGHT = 400, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Цвета
WHITE = (255, 255, 255)

# Фоновое изображение
BG_IMG = pygame.image.load('background.png')
BG_IMG = pygame.transform.scale(BG_IMG, (WIDTH, HEIGHT))

# Птица
BIRD_IMG = pygame.image.load('bird.png')
BIRD_IMG = pygame.transform.scale(BIRD_IMG, (50, 50))
bird_rect = BIRD_IMG.get_rect(center=(50, HEIGHT//2))
bird_movement = 0

# Трубы
PIPE_IMG = pygame.image.load('pipe.png')
PIPE_IMG = pygame.transform.scale(PIPE_IMG, (70, 400))
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [200, 300, 400]

# Очки
score = 0
font = pygame.font.Font(None, 40)

# Функция создания труб
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    new_pipe = PIPE_IMG.get_rect(midbottom=(WIDTH, random_pipe_pos))
    return new_pipe

# Функция движения труб
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

# Функция отображения текста
def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    WIN.blit(img, (x, y))

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 12
        if event.type == SPAWNPIPE:
            pipe_list.append(create_pipe())

    WIN.blit(BG_IMG, (0, 0))

    # Птица
    bird_movement += 0.8
    bird_rect.centery += bird_movement
    WIN.blit(BIRD_IMG, bird_rect)

    # Трубы
    pipe_list = move_pipes(pipe_list)
    for pipe in pipe_list:
        WIN.blit(PIPE_IMG, pipe)

    # Очки
    draw_text(f'Score: {score}', font, WHITE, 10, 10)

    # Столкновения
    for pipe in pipe_list:
        if bird_rect.colliderect(pipe):
            pygame.quit()
            sys.exit()

    if 0 < bird_rect.top < HEIGHT:
        score += 0.01

    pygame.display.update()