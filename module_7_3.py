import string
class WordsFinder:
    def __init__(self, *args):
        self.file_names = args
    def get_all_words(self):
        trans = {',':' ','.':' ','!':' ','?':' ',';':' ','-':' '} # Таблица первода символов
        all_words = {}                                            # Создание пустого словаря
        i = 0                                                     # Счётчик количества входных файлов
        global file_name
        for file_name in self.file_names:
            #print(file_name)
            #print('')
            with open(self.file_names[i], encoding='utf-8') as file: # Открываем файл
                i += 1
                line = file.read().lower()                                   # Чтение из файла
                #line = line.lower()
                line = line.replace('\n', '')
                tbl = line.maketrans(trans)
                line = line.translate(tbl)            # Убираем заданые символы(по таблице трансляции)
                line = line.split(sep=' ')
            all_words = {self.file_names[i-1]: line}  # Заносим данные в словарь
            #print(all_words)
        return all_words
    def find(self, word):
        word = word.lower()
        for name, words  in self.get_all_words().items():
            j = 0  # Счётчик позиции искомого слова
            for j in range(len(words)):
                if word == words[j]:
                    break
            all_words = {self.file_names[0]: j + 1}
        return all_words
    def count(self, word):
        word = word.lower()
        for name, words in self.get_all_words().items():
            j = 0
            kol_vh = 0                       # Количество вхождений искомого слова
            for j in range(len(words)):
                if word == words[j]:
                    kol_vh +=1
            all_words = {self.file_names[0]: kol_vh}
        return all_words

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

