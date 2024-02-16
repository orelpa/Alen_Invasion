import pygame

class Ship():
    #настройка корабля

    def __init__(self, ai_settings, screen):
        """Инициализирует корабль и задает его начальную позициб"""

        self.screen = screen
        self.ai_settings = ai_settings


        #Загрузка изображения корабля и получение прямоугольника
        self.image = pygame.image.load('images/galactica.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #каждый новый корабльь появляется у нижнего каря экрана
        self.rect.centerx = self.screen_rect.centerx    
        self.rect.bottom = self.screen_rect.bottom

        #сохранение вещественной координаты центра коробля
        self.center = float(self.rect.centerx)

        #Флаг перемещение
        self.moving_right = False
        self.moving_left = False

    ship_speed_factor = 1.5
    def update(self):
        """Обновляет позицию корабля с учетом флага"""
            #обновляется атрибут center, не rect
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
        #обновление атрибута rect а основании self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Рисует корабльь в текущей позиции"""
        self.screen.blit(self.image, self.rect)


