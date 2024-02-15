import pygame

class Ship():
    def __init__(self, screen):
        """Инициализирует корабль и задает его начальную позициб"""

        self.screen = screen

        #Загрузка изображения корабля и получение прямоугольника
        self.image = pygame.image.load('images/galactica.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #каждый новый корабльь появляется у нижнего каря экрана
        self.rect.centerx = self.screen_rect.centerx    
        self.rect.bottom = self.screen_rect.bottom

        #Флаг перемещение
        self.moving_right = False
    
    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        """Рисует корабльь в текущей позиции"""
        self.screen.blit(self.image, self.rect)


