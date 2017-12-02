import pygame
from pygame import *  # PyGame модуль

# For fast test
print("For fast test")

def main():
    pass
    pygame.init()  # Инициация PyGame, обязательная строчка
    info_object = pygame.display.Info()
    win_width = info_object.current_w
    win_height = info_object.current_h

    fps = 30
    display = (win_width, win_height)  # Группируем ширину и высоту в одну переменную
    bg_color = "#000000"

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(display)  # Создаем окошко
    pygame.display.set_caption("RS")  # Пишем в шапку
    bg = pygame.Surface(display)
    bg.fill(pygame.Color(bg_color))
    window_mode = True
    running = True


    while running:  # Основной цикл программы
        screen.blit(bg, (0, 0))

        for ev in pygame.event.get():  # Обрабатываем события
            # ALT + F4 - закрытие окна
            if (ev.type == QUIT) or (ev.type == KEYDOWN and (ev.key == K_F4 and ev.mod == 256)): #K_LALT and K_RALT not working
                running = False

            if ev.type is KEYDOWN and ev.key == K_F10:
                if window_mode:  # Если были в оконном режиме - переключаемся в Fullscreen
                    screen = pygame.display.set_mode(display, FULLSCREEN)
                    window_mode = False
                else:  # Если были в Fullscreen режиме - переключаемся в оконный
                    screen = pygame.display.set_mode(display)
                    window_mode = True


        pygame.display.update()  # обновление и вывод всех изменений на экран
        clock.tick(fps)

    pygame.quit()
    exit()

if __name__ == "__main__":
    main()