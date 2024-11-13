import io
from pprint import pprint
class Product:
    global products
    products = ''
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = str(weight)
        self.category = category
    def __str__(self):
        products = self.name+', '+ self.weight+', ' +self.category
        return products

class Shop():
    def get_products(self):
        file = open('products.txt', 'r', encoding='utf-8')
        print(file)
        pprint(file.read())
        file.close()
        #return print(zapas)
    def add(self, *products):               # Добавление продуктов в файл
        file = open('products.txt', 'a', encoding='utf-8')
        file.write('Новый текст\n')
        #rint(self.name)
        print('!!! ---', products[0])
        #file.write('!!!', Product(self.name, self.weight, self.category),'\n')
        file.write('!!!'+ str(products[0])+'\n')
        #file.write(Product.__str__(self.name),'\n')
        #print(Product(self.name, self.weight, self.category))
        #print(Product.__str__(self))
        file.close()






s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')

p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p1)
print(p2)
print(p3)
s1.add(p1, p2, p3)


