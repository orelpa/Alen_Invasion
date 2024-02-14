import sys
import pygame

def run_game():
    """Инициализирует игру и создает объект экрана"""
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    """
    объект screen - назвается поврхностью - часть экрана на которой отображается
    игровой элемент
    """
    pygame.display.set_caption("Alien Invasion")

    #Запуск основного цикла игры
    while True:
        #Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #отображение последнего прорисованного экрана
            pygame.display.flip()

run_game()