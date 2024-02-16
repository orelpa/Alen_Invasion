import sys
import pygame

from settings import Settings
from ship import Ship

import game_functions as gf

def run_game():
    """Инициализирует игру и создает объект экрана"""
    pygame.init()
    
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    """
    объект screen - назвается поврхностью - часть экрана на которой отображается
    игровой элемент
    """
    pygame.display.set_caption("Alien Invasion")
    
    #создание корабля
    ship = Ship(ai_settings, screen)
    
    
    #назначение цвета фона
    

    #Запуск основного цикла игры
    while True:
        #заменяем код на функцию
        gf.check_events(ship)
        ship.update()

        gf.update_screen(ai_settings, screen, ship)
        




run_game()