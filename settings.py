
class Settings():
    """Класс для хранения все настроек"""

    def __init__(self):
        """Инициализирует настройки игры"""
        
        #Параметры экрана
        self.ship_speed_factor = 1.5
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (77, 143, 172)