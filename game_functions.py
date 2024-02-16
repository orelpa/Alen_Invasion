import pygame
import sys

def check_events(ship):
    """Обрабатывает нажатия клавиш и события мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #отслеживаем нажатие клавиш
        elif event.type == pygame.KEYDOWN:

            #если нажата клавиша в право
            if event.key == pygame.K_RIGHT:
                # перемещаем корабль в право
                ship.moving_right = True
        elif event.type == pygame.KEYUP:
            #отпускает кнопку корабль останавливается
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False



def update_screen(ai_settings, screen, ship):
    """Обновляет изображения на экране и отображает новый экран"""
    #при каождом проходе цикла перерисовыается экран
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #Отображение последнего прорисованного экрана
    pygame.display.flip()

