import pygame

class Ball:
    def __init__(self, x, y, radius, screen_width, screen_height):
        # Оборачиваем в int, чтобы координаты всегда были целыми
        self.x = int(x)
        self.y = int(y)
        self.radius = radius
        self.speed = 20
        self.screen_width = screen_width
        self.screen_height = screen_height

    def move(self, dx, dy):
        # Сначала меняем, потом проверяем границы
        self.x += dx
        self.y += dy

        # Проверка границ (чтобы не улетал за экран)
        if self.x - self.radius < 0:
            self.x = self.radius
        if self.x + self.radius > self.screen_width:
            self.x = self.screen_width - self.radius
            
        if self.y - self.radius < 0:
            self.y = self.radius
        if self.y + self.radius > self.screen_height:
            self.y = self.screen_height - self.radius

    def draw(self, screen):
        # Рисуем, принудительно преобразуя координаты в int
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), self.radius)