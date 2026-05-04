import pygame

# 1. Сначала задаем размеры и инициализируем экран
WIDTH, HEIGHT = 800, 800  # Напиши тут свои размеры, которые были в clock.py
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

# 2. ТЕПЕРЬ импортируем логику. 
# Внутри clock.py функции должны вызываться только ПОСЛЕ создания screen
from clock import update 

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заливаем экран, чтобы не оставалось следов от стрелок
    screen.fill((255, 255, 255)) 

    update(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()