import multiprocessing
import time

def read_info(file_name):
    all_data = []
    with open(file_name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if len(line) == 0:  # Проверка на наличие символов в строке
                break
            all_data.append(line)  # Запись строк в список
    print(f'Входной файл: {file_name}, Строк в этом файле: {len(all_data)}')

if __name__ == '__main__':
    file_names = [f'./file {i}.txt' for i in range(1, 5)]   # Список имён входных файлов
    time_start = time.time()                                # Начало движухи

    with multiprocessing.Pool() as pool:                    # Собственно перебор входных файлов
        pool.map(read_info, file_names)

    time_end = time.time()                                  # Движуха завершена
    print()
    print('Общее время выполнения:', time_end - time_start)

