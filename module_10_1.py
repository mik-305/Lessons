import threading
import time
from time import sleep

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write('Какое-то слово № ' + str(i + 1) + '\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

    # ФУНКЦИИ
time_start = time.time()                                    # Начало работы функций
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = time.time()                                      # Конец работы функций
print('Время работы функций: ', time_end - time_start)      # Итоговое время работы функций

    # ПОТОКИ
time_start = time.time()                                    # Начало создания потоков

threads = []

threads.append(threading.Thread(target=write_words, args=(10, 'example5.txt')))
threads.append(threading.Thread(target=write_words, args=(30, 'example6.txt')))
threads.append(threading.Thread(target=write_words, args=(200, 'example7.txt')))
threads.append(threading.Thread(target=write_words, args=(100, 'example8.txt')))

for thread in threads:
    thread.start()                                          # Запуск потоков

for thread in threads:
    thread.join()

time_end = time.time()                                      # Потоки завершили работу

print('Время работы потоков: ', time_end - time_start)
