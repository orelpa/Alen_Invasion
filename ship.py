import pygame

class Ship():
    def __init__(self, screen):
        """Инициализирует корабль и задает его начальную позициб"""

        self.screen = screen

        #Загрузка изображения корабля и получение прямоугольника
        self.image = pygame.image.load('images/ship.bmp')
        self.ract = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #каждый новый корабльь появляется у нижнего каря экрана
        self.rect.centrex = self.screen_rect.centrex
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Рисует корабльь в текущей позиции"""
        self.screen.blit(slef.image, self.rect)

