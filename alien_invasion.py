import sys
import pygame

from settings import Settings

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
    
    #назначение цвета фона
    bg_color = (ai_settings.bg_color)

    #Запуск основного цикла игры
    while True:
        #Отслеживание событий клавиатуры и мыши


        for event in pygame.event.get():
            
            #При каждом проходе цикла перерисовывается экран
            screen.fill(bg_color)
            if event.type == pygame.QUIT:
                sys.exit()
            #отображение последнего прорисованного экрана
            pygame.display.flip()

run_game()