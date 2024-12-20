import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name} на нас напали!')
        i = 1  # Счетчик дней
        enemies = 100  # Количество врагов у КАЖДОГО рыцаря


        while enemies > 0:      # Если остались враги, продолжаем сражаться
            enemies = max(0, enemies - self.power)  # Счетчик оставшихся врагов
            print(f'\n{self.name} сражается {i} дней(дня)..., осталось {enemies} воинов.')
            time.sleep(1)  # ВременнАя задержка
            i += 1         # Дни сражения

        print(f'{self.name} одержал победу спустя {i - 1} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)           # Создаем рыцарей
second_knight = Knight('Sir Galahad', 20)           # Создаем рыцарей


first_knight.start()         # Поток для первого рыцаря
second_knight.start()        # Поток для второго рыцаря


first_knight.join()         # Ожидание завершения потоков
second_knight.join()        # Ожидание завершения потоков

print('Все битвы закончились!')




