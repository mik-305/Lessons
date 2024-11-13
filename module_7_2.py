import io
from pprint import pprint
def custom_write(file_name, *args):
    strings_positions = {}
    file = open(file_name, 'a', encoding='utf-8')       # Открыт файл
    i = 0
    flag_file = file.tell()                             # Позиция указателя в файле
    for i in range(len(info)):
        flag_file = file.tell()
        strings_positions[i+1, file.tell()] = info[i]   # Заполняем словарь
        file.write(info[i] + '\n')                      # Пишем в файл
    file.close()
    return strings_positions


info = ['Text for tell.','Используйте кодировку utf-8.',
    'Because there are 2 languages!', 'Спасибо!']

result = custom_write('text.txt', info)
for elem in result.items():
    print(elem)