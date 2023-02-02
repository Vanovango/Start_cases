import pygame

from settings import Settings


class Ship:
    """Класс для управления кораблем."""

    def __init__(self, screen):
        """Инициализирует корабль и задает его начальную позицию."""

        self.settings = Settings()

        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение вещественной координаты центра корабля.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.settings = Settings()

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right and self.rect.right < self.settings.screen_width:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        if self.moving_down and self.rect.bottom < self.settings.screen_height:
            self.y += self.settings.ship_speed

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        # Обновление атрибута rect на основании self.x.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
