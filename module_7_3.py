class WordsFinder:

    all_words = {}  # Создание пустого словаря
    def __init__(self, *args):
        self.file_names = args
    def get_all_words(self):
        i = 0                               # Счётчик количества входных файлов
        with open(self.file_names[i], encoding='utf-8') as file:
            global line
            line = file.read()              # Чтение из файла
            line = line.lower()             # Перевод в нижнйи регистр
            line = line.replace(',', ' ')
            line = line.replace('!', ' ')
            line = line.replace('=', ' ')
            line = line.replace('.', ' ')
            line = line.replace('?', ' ')
            line = line.replace(';', ' ')
            line = line.replace(':', ' ')
            line = line.replace('-', ' ')
            line = line.replace('\n', '')
            line = line.split(sep=' ')
        all_words = {self.file_names[0]: line}      # Заносим данные в словарь
        return all_words

    def find(self, word):
        nom_in_str = 0                              # Номер искомого слова
        line_str = str(line)
        words = line_str.split(' ')
        for j in range(len(words)):
            if words[j].find(word.lower()) != -1:
                nom_in_str = j+1
                break
        all_words = {self.file_names[0]: nom_in_str}
        return all_words

    def count(self, word):
        line_str = str(line)
        kol_sovp = 0                        # Количество нахождений искомого слова
        words = line_str.split(' ')
        for j in range(len(words)):
            if word.lower() in words[j].lower():
                kol_sovp +=1
        all_words = {self.file_names[0]: kol_sovp}
        return all_words





finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего


