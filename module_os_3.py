import time
import os
import os.path
from datetime import datetime

directory = 'c:\\intel\\Logs\\'                                     # Директорий для примера

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)                         # Путь к файлу
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime)) # Дата и время изменения файла
        filesize = os.path.getsize(filepath)                        # Размер файла
        parent_dir = os.path.dirname(filepath)                      # Родительская директория
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
        f'Родительская директория: {parent_dir}')

