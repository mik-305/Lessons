#import multiprocessing
import time

def read_info(name):
    all_data = []
    with open(name[number - 1], 'r', encoding='utf-8') as file:
        while True:
            stroka = file.readline()
            if len(stroka) == 0:             # Пока считаная строка не пустая
                break
            all_data.append(stroka)          # Содержимое строки файла записываем в переменную
        print('     Имя входного файла '+name[number-1]+' Строк в файле ', len(all_data))

name = [f'./file {number}.txt' for number in range(1, 5)]
time_start = time.time()        # Начало обработки

for number in range(1, 5):
    read_info(name)

time_end = time.time()          # Финиш обработки
print()
print('Общее время работы : ', time_end - time_start)  # Итоговое время работы
