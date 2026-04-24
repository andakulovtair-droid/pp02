import pygame
import math
import time
import os

WIDTH, HEIGHT = 600, 600
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 230

BASE_DIR = os.path.dirname(__file__)
img_path = os.path.join(BASE_DIR, "images", "mickey_hand.png")

hand = pygame.image.load(img_path).convert_alpha()


def blit_rotate(surface, image, pivot, angle):
    image_rect = image.get_rect()
    pivot_vector = pygame.math.Vector2(pivot) - image_rect.center

    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_rect = rotated_image.get_rect()

    rotated_vector = pivot_vector.rotate(angle)

    rotated_rect.center = (CENTER[0] - rotated_vector.x,
                           CENTER[1] - rotated_vector.y)

    surface.blit(rotated_image, rotated_rect)


def draw_clock(screen):
    pygame.draw.circle(screen, (0, 0, 0), CENTER, RADIUS, 3)

    for i in range(12):
        a = math.radians(i * 30 - 90)
        x = CENTER[0] + (RADIUS - 15) * math.cos(a)
        y = CENTER[1] + (RADIUS - 15) * math.sin(a)
        pygame.draw.circle(screen, (0, 0, 0), (int(x), int(y)), 5)


# подготовка стрелок
sec_hand = pygame.transform.scale(hand, (100, 260))
sec_hand = pygame.transform.flip(sec_hand, True, False)

min_hand = pygame.transform.scale(hand, (80, 200))

pivot_sec = (sec_hand.get_width() // 2, sec_hand.get_height())
pivot_min = (min_hand.get_width() // 2, min_hand.get_height())


def update(screen):
    t = time.localtime()

    sec_angle = t.tm_sec * 6
    min_angle = t.tm_min * 6

    screen.fill((255, 255, 255))
    draw_clock(screen)

    blit_rotate(screen, min_hand, pivot_min, min_angle)
    blit_rotate(screen, sec_hand, pivot_sec, sec_angle)