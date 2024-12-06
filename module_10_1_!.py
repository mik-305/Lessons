import threading
import time
from time import sleep

def write_words(word_count, file_name):
    file = open(file_name , 'w',  encoding='utf-8')
    for i in range(word_count):
        file.write('Какое-то слово № '+ str(i+1)+'\n')
        time.sleep(0.1)
    print('Завершилась запись в файл '+file_name)
    file.close()
'''
time_start = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = time.time()
print('Время работы: ', time_end - time_start)'''


time_start = time.time() 
thread = threading.Thread(target = write_words, args = (10, 'example5.txt' ))
thread.start()
#thread.join()

thread = threading.Thread(target = write_words, args = (30, 'example6.txt' ))
thread.start()
#thread.join()

thread = threading.Thread(target = write_words, args = (200, 'example7.txt' ))
thread.start()
#thread.join()

thread = threading.Thread(target = write_words, args = (100, 'example8.txt' ))
thread.start()
#thread.join()


time_end = time.time()
print('Время работы потоков: ', time_end - time_start)




