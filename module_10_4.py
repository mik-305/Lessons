import threading
import time
import random
from queue import Queue

class Table:                                        # Класс Table
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):                      # Класс Guest
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))   # Ожидание от 3 до 10 сек

class Cafe:                                         # Класс Cafe
    def __init__(self, *tables):
        self.tables = list(tables)
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            free_table = next((table for table in self.tables if table.guest is None), None)
            if free_table:
                free_table.guest = guest
                guest.start()
                print(f"{guest.name} сел(-а) за стол № {free_table.number}")
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол № {table.number} свободен")
                    table.guest = None

                if not self.queue.empty() and table.guest is None:
                    next_guest = self.queue.get()
                    table.guest = next_guest
                    next_guest.start()
                    print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол № {table.number}")
            time.sleep(1)

if __name__ == '__main__':
    cafe = Cafe(Table(1), Table(2), Table(3), Table(4), Table(5), Table(6))     # Заполнение кафе столами
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]                                                           # Имена ожидаемых гостей
    guests = [Guest(name) for name in guests_names]             # Создание гостей
    cafe.guest_arrival(*guests)                                 # Приём гостей
    cafe.discuss_guests()                                       # Обслуживание гостей
    print("Кафе завершило обслуживание гостей.")
