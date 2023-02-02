class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (0, 0, 0)

        # Настройки корабля
        self.ship_speed = 1

        # Параметры снаряда
        self.bullet_speed = 1.5
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (255, 60, 60)
        self.bullets_allowed = 10

        # Настройки пришельцев
        self.alien_speed = 0.
        self.fleet_drop_speed = 0.
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1
