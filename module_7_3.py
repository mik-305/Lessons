class WordsFinder:
    def __init__(self, *args):
        self.file_names = args
        #self.word = word
        return

    def get_all_words(self):
        all_words = {}                      # Создание пустого словаря
        i = 0
        with open(self.file_names[i], encoding='utf-8') as file:
            i += 1
            line_str = ''
            kol_strok = 0                   # Счетчик строк в файле
            for line in file:               # Считываем файл построчно
                kol_strok +=1
                line = line.lower()
                line = line.replace(',',' ')
                line = line.replace('!', ' ')
                line = line.replace('=', ' ')
                line = line.replace('.', ' ')
                line = line.replace('?', ' ')
                line = line.replace(';', ' ')
                line = line.replace(':', ' ')
                line = line.replace('-', ' ')

                for j in range(len(line)):
                    line_str = line_str + line[j]
            line_str = line_str.split(sep=' ')  # СТРОКА, РАЗД. ПРОБЕЛАМИ
            all_words = {self.file_names: line_str}
        return all_words

    def find(self, word):
        pass
        return word
        print('Входной аргумент', word)
    #`print(word)`





finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту


