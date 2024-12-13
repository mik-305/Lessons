import string
class WordsFinder:

    def __init__(self, *args):
        trans = {',': ' ', '.': ' '}

        all_words = {}                              # Создание пустого словаря
        self.file_names = args
        i = 0                                       # Счётчик входных файлов
        for file_name in self.file_names:
            print(file_name)
            print('')
            with open(self.file_names[i], encoding='utf-8') as file:
                i += 1
                line = file.read()                  # Чтение из файла
                line = line.lower()                 # Перевод в нижнйи регистр
                line = line.replace('\n', '')
                print('  ДО: ',line)
                line = line.maketrans(trans)

                """for char in string.punctuation:
                    if char in line:
                        # банальная замена символа в строке
                        #line = line.replace(char, '.')
                        pass"""

                print('ПОСЛЕ:', line)



finder2 = WordsFinder('test_file.txt'   )
