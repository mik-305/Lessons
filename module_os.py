import time
import os
from datetime import datetime

directory = os.getcwd()
print('Наш текущий директорий',os.getcwd())
filetime = time.time()
formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
print('Текущая дата и время: ', formatted_time)
print('Содержимое нашего директория', os.listdir())
print('')
print('Составной путь: ', os.path.join('C:\\Users\\it07\\', 'PycharmProjects\\Bot_Lesson\\pythonBot_Lesson\\', 'example1.txt'))
filename = 'C:\\Users\\it07\\PycharmProjects\\Bot_Lesson\\pythonBot_Lesson\\example1.txt'   #
ctime = os.stat(filename).st_ctime
ctime_readable = datetime.fromtimestamp(ctime)
print('Дата создания файла:', ctime_readable)                       # Дата создания
mtime = os.path.getmtime(filename)
mtime_readable = datetime.fromtimestamp(mtime)
print('Дата последнего изменения файла' , mtime_readable)           # Дата последнего измемения
file_size = os.path.getsize('C:\\Users\\it07\\PycharmProjects\\Bot_Lesson\\pythonBot_Lesson\\example1.txt')
print('Размер файла:', file_size, 'байт')
print('')
print('Родительский директорий: ' ,os.path.dirname('C:\\Users\\it07\\PycharmProjects\\Bot_Lesson\\pythonBot_Lesson\\example1.txt'))

