import threading
import random
import time

class Bank():
    lock = threading.Lock()
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()  # Локальный lock для каждого объекта

    def deposit(self):
        for i in range(100):
            slu_chisl = random.randint(50, 500)         # Случайное число для пополнения баланса
            if (self.balance >= 500) and self.lock.locked():
                self.lock.release()
            self.balance = self.balance + slu_chisl
            print(f" Пополнение на: {slu_chisl}. Баланс: {self.balance}")
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            slu_chisl = random.randint(50, 500)  # Случайное число для снятия с баланса
            print(f"Запрос на {slu_chisl}")
            if slu_chisl <= self.balance:
                self.balance = self.balance - slu_chisl
                print( f"Снятие: {slu_chisl}. Баланс: {self.balance}")
            else:
                print(f"Запрос отклонён, средств недостаточно")
                self.lock.acquire()

            time.sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'   Итоговый баланс: {bk.balance}')