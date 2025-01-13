import requests

class obj:
    def __init__(self):
       self.attrubute_1 = 77
    def some_class_metod(self, value):
        self.attrubute_1 = value
        print(self.attrubute_1)

def introspection_info(obj):
    pass

def some_function(param, param2 = 'XXX'):
    print(f'Мои параметры: ', param, param2)

some_string = 'Некая строка'
some_number = 77
some_list = [1,2,3,4,5]

print(obj.some_class_metod.__name__)
print(obj.some_class_metod)
print(type(obj))

#print(obj.some_class_metod.__name__)


a = some_function('AAA')